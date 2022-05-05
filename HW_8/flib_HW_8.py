from random import choice

WIN_RULES = {
     'камень': ('ящерица', 'ножницы'),
     'ножницы': ('бумага', 'ящерица'),
     'бумага': ('камень', 'спок'),
     'ящерица': ('спок', 'бумага'),
     'спок': ('ножницы', 'камень')
}

counter_user_wins = 0
counter_computer_wins = 0


def get_user_choice():
    '''
    Функция запрашивает у Игрока ввод данных и проводит валидацию
    :return: данные о выборе Игрока в формате 'str'
    '''
    while True:
        user_choice = input('Сделайте свой выбор (камень, ножницы, бумага, ящерица, спок) или введите "стоп": ')
        user_choice = user_choice.lower().strip()
        if user_choice not in WIN_RULES.keys() and user_choice != 'стоп':
            print('Не верный ввод')
            continue
        else:
            return user_choice


def get_computer_choice():
    '''
    Функция генерирует выбор Компьютера из вариантов WIN_RULES.keys
    :return: данные о выборе Компьютера в формате 'str'
    '''
    computer_choice = choice(list(WIN_RULES.keys()))
    return computer_choice


def get_winner(user_choice, computer_choice):
    '''
    Функция принимает данные о выборе Игрока и Компьютера, анализирует и отдаёт данные о результате игры (победителе)
    Так же записывает количество побед Игрока и Компьютера в counter_user_wins и counter_computer_wins
    :param user_choice: данные о выборе Игрока в формате 'str'
    :type: 'str'
    :param computer_choice: данные о выборе Компьютера в формате 'str'
    :type: 'str'
    :return: результат игры (победитель) в формате 'str'
    '''
    if user_choice == computer_choice:
        msg = 'Ничья'
        return msg

    for i in WIN_RULES[user_choice]:
        if i == computer_choice:
            msg = 'Игрок'
            global counter_user_wins
            counter_user_wins += 1
            return msg

    msg = 'Компьютер'
    global counter_computer_wins
    counter_computer_wins += 1
    return msg


def stop_choice():
    '''
    Функция запускается в случае выбора Игроком варианта "стоп" и выводит сообщение со статистикой игр
    '''
    print('Итог игры:')
    if counter_computer_wins == counter_user_wins:
        print(f'Ничья со счётом {counter_user_wins} : {counter_computer_wins}')
    elif counter_computer_wins > counter_user_wins:
        print(f'Компьютер победил со счётом {counter_computer_wins} : {counter_user_wins}')
    else:
        print(f'Игрок победил со счётом {counter_user_wins} : {counter_computer_wins}')


def make_message(user_choice, computer_choice, winner):
    '''
    Функция принимает данные о выборе Игрока, Компьютера и результате игры (победителе), и выводит сообшение
    содержащее выбор Игрока, выбор Компьютера и результат игры (победитель)
    :param user_choice: данные о выборе Игрока в формате 'str'
    :type: 'str'
    :param computer_choice: данные о выборе Компьютера в формате 'str'
    :type: 'str'
    :param winner: результат игры (победитель) в формате 'str'
    :type: 'str'
    '''
    print(f'Игрок выбрал {user_choice}, Компьютер выбрал {computer_choice}.')
    if winner == 'Ничья':
        print('Ничья!')
    else:
        print(f'Победил {winner}!')


def start_game():
    '''
    Функция, вызов которой запусткает игру
    '''
    while True:
        user_choice = get_user_choice()
        if user_choice == 'стоп':
            stop_choice()
            break

        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)
        make_message(user_choice, computer_choice, winner)