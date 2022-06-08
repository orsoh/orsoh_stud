import datetime
from Banks_libr import choice_city
from Banks_libr import connect_with_bank
from Banks_libr import BankRequst
from Banks_libr import write_to_logs

def start():
    for_logs = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S \n'))
    write_to_logs(for_logs)
    chosen_city = choice_city()
    bank_request = connect_with_bank(chosen_city)
    data_from_bank = BankRequst(bank_request)
    while True:
        user_choice = input('Введите "курс" для отображения курса \n'
                            'Введите "инфо" для отображения информации об отделение банка\n'
                            '---> ').lower().strip()
        if user_choice != 'курс' and user_choice != 'инфо':
            print('Не верный ввод')
            continue
        elif user_choice == 'курс':
            data_from_bank.get_exchange_currency
        elif user_choice == 'инфо':
            data_from_bank.get_depart_info

start()
