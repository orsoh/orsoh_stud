

def get_user_choice():
    while True:
        user_choice = input('Сделайте свой выбор (камень, ножницы, бумага, ящерица, спок) или введите "стоп": ')
        user_choice = user_choice.lower().strip()
        if user_choice not in WIN_RULES.keys() and user_choice != 'стоп':
            print('Не верный ввод')
            continue
        else:
            return user_choice


def get_computer_choice():
    computer_choice = choice(list(WIN_RULES.keys()))
    return computer_choice


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        msg = 'Ничья'
        return msg

    for i in WIN_RULES[user_choice]:
        if i == computer_choice:
            msg = 'Игрок'
            global counter_user_wins
            counter_user_wins += 1
            return msg
        else:
            msg = 'Компьютер'
            global counter_computer_wins
            counter_computer_wins += 1
            return msg


def stop_choice():
    print('Итог игры:')
    if counter_computer_wins == counter_user_wins:
        print(f'Ничья со счётом {counter_user_wins} : {counter_computer_wins}')
    elif counter_computer_wins > counter_user_wins:
        print(f'Компьютер победил со счётом {counter_computer_wins} : {counter_user_wins}')
    else:
        print(f'Игрок победил со счётом {counter_user_wins} : {counter_computer_wins}')


def make_message(user_choice, computer_choice, winner):
    print(f'Игрок выбрал {user_choice}, Компьютер выбрал {computer_choice}.')
    if winner == 'Ничья':
        print('Ничья!')
    else:
        print(f'Победил {winner}!')


def start_game():
    while True:
        user_choice = get_user_choice()
        if user_choice == 'стоп':
            stop_choice()
            break

        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)
        make_message(user_choice, computer_choice, winner)