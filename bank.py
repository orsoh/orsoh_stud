import requests
import datetime

city_catalog = ( 'Минск', 'Брест', 'Витебск', 'Гомель', 'Могилёв', 'Гродно')


def write_to_errors(error_list):
    with open('error_list.txt', mode='at') as errors:
        data = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S \n'))
        for_error = f' {error_list}'
        errors.write(data)
        errors.write(for_error)


def choice_city():
    for city in city_catalog:
        print(city)
    while True:
        chosen_city = input('Введите город -->').capitalize()
        if chosen_city not in city_catalog:
            print('Не верный ввод')
            continue
        else:
            for_logs = f'Выбран город {chosen_city}'
            return for_logs, chosen_city


def connect_with_bank(chosen_city):
    print('Соединение...')
    try:
        bank_request = requests.request('GET', f'https://belarusbank.by/api/kursExchange?city={chosen_city}')
    except Exception as error_list:
        print(bank_request.status_code)
        print('Соединение не удалось')
        write_to_errors(error_list)
        return

    if 300 > bank_request.status_code >= 200 and bank_request.headers.get('Content-Type') == 'application/json; charset=utf-8':
        return bank_request
    else:
        print('Ошибка типа контента')
        print(bank_request.headers.get('Content-Type'))
        return


class BankRequst():

    content = None

    _for_exchange_currency = ('USD_in', 'USD_out', 'EUR_in', 'EUR_out', 'RUB_in', 'RUB_out', 'GBP_in', 'GBP_out',
                              'CAD_in', 'CAD_out', 'PLN_in', 'PLN_out', 'UAH_in', 'UAH_out', 'SEK_in', 'SEK_out',
                              'CHF_in', 'CHF_out', 'JPY_in', 'JPY_out', 'CNY_in', 'CNY_out', 'CZK_in', 'CZK_out',
                              'NOK_in', 'NOK_out', 'USD_EUR_in', 'USD_EUR_out', 'USD_RUB_in', 'USD_RUB_out',
                              'RUB_EUR_in', 'RUB_EUR_out')

    _for_depart_info = ('filial_id', 'info_worktime', 'street_type', 'filials_text', 'home_number', 'name', 'name_type',
                        'street', 'sap_id')

    def __init__(self, init_content):
        self.bank_content = init_content

    @property
    def bank_content(self):
        return self.content

    @bank_content.setter
    def bank_content(self, new_content):
        if not isinstance(new_content, (requests.models.Response)):
            raise TypeError
        try:
            self.content = new_content.json()
        except Exception as error_list:
            write_to_errors(error_list)
            print('Ошибка типа контента')
            return

    def choise_department(self):
        departments_catalog = {}
        for departments in self.content:
            for key, val in departments.items():
                if key == 'filials_text':
                    departments_catalog[val] = departments

        for departments in departments_catalog.keys():
            print(departments)

        while True:
            choise_department = input('Выберете отделение ---> ": ')
            choise_department = choise_department.strip()
            if choise_department not in departments_catalog.keys():
                print('Не верный ввод')
                continue
            else:
                chosen_department = departments_catalog[choise_department]
                return chosen_department

    @property
    def get_exchange_currency(self):
        exchange_currency = {}
        chosen_department = self.choise_department()
        for currency in self._for_exchange_currency:
            try:
                exchange_currency[currency] = chosen_department[currency]
            except Exception as error_list:
                write_to_errors(error_list)
                continue
        return exchange_currency

    @property
    def get_depart_info(self):
        department_info = {}
        chosen_department = self.choise_department()
        for info in self._for_depart_info:
            try:
                department_info[info] = chosen_department[info]
            except Exception as error_list:
                write_to_errors(error_list)
                continue
        return department_info




with open('logs.txt', mode='at') as logs:
    data = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S \n'))
    otdl = f'{user_choice} \n'
    msg = f'\n' \
          f'{data} {otdl}'
    logs.write(msg)
    for k, v in choise_otdel.items():
        log = f'{k} - {v} \n'
        logs.write(log)


