def input_fun():
    while True:
        client_age = input('Укажите свой полный возраст ---> ').replace(' ', '').lstrip('0')
        try:
            client_age_int = int(client_age)
            if client_age_int > 130:
                print('Не верный возраст')
                continue
            break
        except:
            print('Не верный ввод данных')
    return client_age


def msg_part_fun(client_age):
    """
    """
    age_cool = client_age.count(client_age[0]) == len(client_age)
    if len(client_age) == 1:
        age_cool = not age_cool
    client_age_int = int(client_age)
    if client_age_int < 7:
        msg_part = 'Тебе же {age_part}! Где твои родители?'
    elif client_age_int < 16 and not age_cool:
        msg_part = 'Тебе всего лишь {age_part}, а это фильм для взрослых'
    elif client_age_int > 65 and not age_cool:
        msg_part = 'Вам {age_part}? Покажите пенсионное удостоверение'
    elif age_cool:
        msg_part = 'О, вам {age_part}? Какой интересный возраст!'
    else:
        msg_part = 'Не смотря на то что вам {age_part}, билетов всё равно нет!'
    return msg_part


def age_part_fun(client_age):
    client_age_int = int(client_age)
    if 9 < client_age_int < 20:
        age = f'{client_age_int} лет'
    else:
        if 4 < int(client_age[-1]) < 10 or int(client_age[-1]) == 0:
            age = f'{client_age_int} лет'
        elif 1 < int(client_age[-1]) < 5:
            age = f'{client_age_int} года'
        else:
            age = f'{client_age_int} год'
    return age

client_age = input_fun()
msg = msg_part_fun(client_age)
age = age_part_fun(client_age)
res_str = msg.format(age_part=age)
print(res_str)