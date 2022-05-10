from random import choice
import datetime

WIN_RULES = {
     'камень': ('ящерица', 'ножницы'),
     'ножницы': ('бумага', 'ящерица'),
     'бумага': ('камень', 'спок'),
     'ящерица': ('спок', 'бумага'),
     'спок': ('ножницы', 'камень')
}

wins_counter = {
    'counter_user_wins': 0,
    'counter_computer_wins': 0,
    'games_counter': 0
}

def write_to_logs(fun):
    '''
    Декоратор записывающий данные в logs.txt
    '''
    def wrapper(*args, **kwargs):
        with open('logs.txt', mode='at') as logs:
            wins_counter['games_counter'] = wins_counter['games_counter'] + 1
            game = wins_counter['games_counter']
            data = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            msg = fun(*args, **kwargs)
            log = f'{game} {data} {msg}'
            logs.write(log)

    return wrapper



def get_user_choice():
    '''
    Функция запрашивает у Игрока ввод данных и проводит валидацию
    :return: данные о выборе Игрока в формате 'str'
    '''
    while True:
        user_choice = input('Сделайте свой выбор (камень, ножницы, бумага, ящерица, спок) или введите "стоп"\n'
                            'Для просмотра статистики введите "стат"\n'
                            '---> ').lower().strip()

        if user_choice not in WIN_RULES.keys() and user_choice != 'стоп' and user_choice != 'стат':
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
    Так же записывает количество побед Игрока и Компьютера в wins_counter
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
            wins_counter['counter_user_wins'] = wins_counter['counter_user_wins'] + 1
            return msg

    msg = 'Компьютер'
    wins_counter['counter_computer_wins'] = wins_counter['counter_computer_wins'] + 1
    return msg


@write_to_logs
def stop_choice():
    '''
    Функция запускается в случае выбора Игроком варианта "стоп" и выводит сообщение со статистикой игр
    :return: Данные со статистикой игры в формате str
    '''
    user = wins_counter['counter_user_wins']
    computer = wins_counter['counter_computer_wins']
    msg1 = 'Итог игры: '
    print(msg1)

    if user == computer:
        msg2 = (f'Ничья со счётом {user} : {computer}\n')
        print(msg2)
    elif computer > user:
        msg2 = (f'Компьютер победил со счётом {computer} : {user}\n')
        print(msg2)
    else:
        msg2 = (f'Игрок победил со счётом {user} : {computer}\n')
        print(msg2)

    msg = msg1 + msg2

    return msg


@write_to_logs
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
    :return: Данные о результате текущей игры в формате str
    '''
    msg1 = (f'Игрок выбрал {user_choice}, Компьютер выбрал {computer_choice}. ')
    print(msg1)
    if winner == 'Ничья':
        msg2 = ('Ничья!\n')
    else:
        msg2 = (f'Победил {winner}!\n')
    print(msg2)
    msg = msg1 + msg2

    return msg


def stat_fun():
    '''
    Функция запускается при выборе Игроком варианта "стат", позволяет просматривать и очищать статистику
    '''
    with open('logs.txt', mode='rt') as logs:
            print(logs.read())

    while True:
        user_choice = input('Для выхода из просмотра статистики введите "выход"\n'
                            'Для очистки статистики введите "очистить"\n'
                            '--->').lower().strip()

        if user_choice == "выход":
            return
        elif user_choice == "очистить":
            with open('logs.txt', mode='w') as logs:
                wins_counter['games_counter'] = 0
                wins_counter['counter_user_wins'] = 0
                wins_counter['counter_computer_wins'] = 0
                logs.write('Новая сессия\n')
            return
        else:
            print('Не верный ввод')
            continue