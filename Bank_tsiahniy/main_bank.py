import datetime
from Banks_libr import choice_city
from Banks_libr import connect_with_bank
from Banks_libr import BankRequst
from Banks_libr import write_to_logs

def start():
    '''
    Запускает выполнение программы
    '''
    for_logs = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S \n'))
    write_to_logs(for_logs)
    while True:
        chosen_city = choice_city()
        if chosen_city == 'Выход':
            for_logs = 'Выход\n'
            write_to_logs(for_logs)
            return
        bank_request = connect_with_bank(chosen_city)
        if bank_request == None:
            continue
        try:
            data_from_bank = BankRequst(bank_request)
        except TypeError:
            print('Ошибка типа данных')
            continue
        while True:
            user_choice = input('Введите "курс" для отображения курса \n'
                                'Введите "инфо" для отображения информации об отделение банка\n'
                                'Введите "назад" для возвращения к выбору города\n'
                                '---> ').lower().strip()
            if user_choice != 'курс' and user_choice != 'инфо' and user_choice != 'назад':
                print('Не верный ввод')
                continue
            elif user_choice == 'курс':
                data_from_bank.get_exchange_currency
            elif user_choice == 'инфо':
                data_from_bank.get_depart_info
                for_logs = 'Запрос информации\n'
                write_to_logs(for_logs)
            elif user_choice == 'назад':
                break
start()
