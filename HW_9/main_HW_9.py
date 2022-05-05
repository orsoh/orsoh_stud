# Доопрацюйте гру з заняття таким чином, щоб вона відповідала розширеним правилам (пояснення).
# Винесіть усі допоміжні функції (окрім main) в окремий файл, (нехай буде lib.py) і виконайте імпорт цих функцій.

from flib_HW_9 import get_computer_choice
from flib_HW_9 import get_user_choice
from flib_HW_9 import stop_choice
from flib_HW_9 import make_message
from flib_HW_9 import get_winner
from flib_HW_9 import time_calc

def start_game():
    '''
    Функция, вызов которой запускает игру
    '''
    while True:
        user_choice = get_user_choice()
        if user_choice == 'стоп':
            stop_choice()
            break

        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)
        make_message(user_choice, computer_choice, winner)

#start_game()


@time_calc
def func():
    z = 0
    for i in range(10000):
        z = z + (i ** i) - (i ** i)
    print(z)


func()
