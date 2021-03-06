import requests
import datetime

city_catalog = ('Минск', 'Брест', 'Витебск', 'Гомель', 'Могилёв', 'Гродно')


def write_to_errors(error_list):
    '''
    Записывает в файл 'error_list.txt' информацию об ошибках
    :param error_list:  переменная содержащая информацию об ошибках
    '''
    with open('error_list.txt', mode='at') as errors:
        data = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S \n'))
        for_error = f' {error_list}'
        errors.write(data)
        errors.write(for_error)
        errors.write('\n')


def write_to_logs(for_logs):
    '''
    Записывает в файл 'logs.txt' содержимое переменной for_logs
    '''
    with open('logs.txt', mode='at') as logs:
        logs.write(for_logs)


def choice_city():
    '''
    Функция позволяющая пользователю выбрать город из списка городов
    :return: возвращает название города в формате str
    '''
    for city in city_catalog:
        print(city)
    while True:
        chosen_city = input('Введите город или\n'
                            'Введите "выход" для завершения работы -->').capitalize()
        if chosen_city not in city_catalog and chosen_city != 'Выход':
            print('Не верный ввод')
            continue
        elif chosen_city == 'Выход':
            return 'Выход'
        else:
            for_logs = f'Выбран город {chosen_city} \n'
            write_to_logs(for_logs)
            return chosen_city


def connect_with_bank(chosen_city):
    '''
    Устанавливает связь с сервером в зависимости от выбранного города
    :param chosen_city: Название города в формате str
    :return: данные с сервера в формате requests.models.Response или None в случае ошибки
    '''
    print('Соединение...')
    try:
        bank_request = requests.request('GET', f'https://belarusbank.by/api/kursExchange?city={chosen_city}')
    except Exception as error_list:
        print('Соединение не установлено')
        write_to_errors(error_list)
        return
    if 300 > bank_request.status_code >= 200 and bank_request.headers.get(
            'Content-Type') == 'application/json; charset=utf-8':
        print('Установлено')
        return bank_request
    else:
        print('Ошибка данных')
        print(bank_request.status_code)
        msg = bank_request.headers.get('Content-Type')
        print(msg)
        error_list = f'Ошибка данных {msg}'
        write_to_errors(error_list)
        return


class BankRequst():

    content = None

    _for_exchange_currency = ('USD_in', 'USD_out', 'EUR_in', 'EUR_out', 'RUB_in', 'RUB_out', 'GBP_in', 'GBP_out',
                              'CAD_in', 'CAD_out', 'PLN_in', 'PLN_out', 'UAH_in', 'UAH_out', 'SEK_in', 'SEK_out',
                              'CHF_in', 'CHF_out', 'JPY_in', 'JPY_out', 'CNY_in', 'CNY_out', 'CZK_in', 'CZK_out',
                              'NOK_in', 'NOK_out', 'USD_EUR_in', 'USD_EUR_out', 'USD_RUB_in', 'USD_RUB_out',
                              'RUB_EUR_in', 'RUB_EUR_out')

    _for_depart_info = ('filials_text', 'name_type', 'name', 'street_type', 'street', 'home_number', 'info_worktime',
                        'sap_id', 'filial_id')

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
        '''
        Позволяет пользователю выбрать отделение банка из списка
        :return: название отделения в формате str
        '''
        departments_catalog = {}
        for departments in self.content:
            for key, val in departments.items():
                if key == 'filials_text':
                    departments_catalog[val] = departments

        for departments in departments_catalog.keys():
            print(departments)

        while True:
            choise_department = input('Выберете отделение или введите "назад" ---> ')
            choise_department = choise_department.strip()
            if choise_department not in departments_catalog.keys() and choise_department != 'назад':
                print('Не верный ввод')
                continue
            elif choise_department == 'назад':
                return
            else:
                chosen_department = departments_catalog[choise_department]
                for_logs = f'{choise_department} \n'
                write_to_logs(for_logs)
                return chosen_department


    @property
    def get_exchange_currency(self):
        '''
        Функция выводящая на экран информацию о курсе валют в выбранном отделении банка
        :return: информация о курсе в формате dict или None если операция отменена
        '''
        exchange_currency = {}
        chosen_department = self.choise_department()
        if chosen_department == None:
            return

        for currency in self._for_exchange_currency:
            try:
                exchange_currency[currency] = chosen_department[currency]
            except Exception as error_list:
                write_to_errors(error_list)
                continue

        for currency, value in exchange_currency.items():
            for_logs = f'{currency} - {value} \n'
            write_to_logs(for_logs)
            print(for_logs)
        return exchange_currency


    @property
    def get_depart_info(self):
        '''
        Функция выводящая на экран информацию об выбранном отделении банка
        :return: информация об отделении банка в формате dict или None если операция отменена
        '''
        department_info = {}
        chosen_department = self.choise_department()
        if chosen_department == None:
            return
        for info in self._for_depart_info:
            try:
                department_info[info] = chosen_department[info]
            except Exception as error_list:
                write_to_errors(error_list)
                continue
        for info, value in department_info.items():
            for_print = f'{info} - {value} \n'
            print(for_print)
        return department_info