# Доопрацюйте гру з заняття таким чином, щоб вона відповідала розширеним правилам (пояснення).
# Винесіть усі допоміжні функції (окрім main) в окремий файл, (нехай буде lib.py) і виконайте імпорт цих функцій.

from flib_HW_10 import get_computer_choice
from flib_HW_10 import get_user_choice
from flib_HW_10 import stop_choice
from flib_HW_10 import make_message
from flib_HW_10 import get_winner
from flib_HW_10 import stat_fun
import datetime

def start_game():
    '''
    Функция, вызов которой запускает игру
    '''
    with open('logs.txt', mode='at') as logs:
        data = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        log = f'{data} Новая сессия\n'
        logs.write(log)

    while True:
        user_choice = get_user_choice()
        if user_choice == 'стоп':
            stop_choice()
            break
        if user_choice == 'стат':
            stat_fun()
            continue

        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)
        make_message(user_choice, computer_choice, winner)

    with open('logs.txt', mode='at') as logs:
        data = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        log = f'{data} Конец сессии\n'
        logs.write(log)

start_game()