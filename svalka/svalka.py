
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


def logic_fun(client_age):
    age_cool = client_age.count(client_age[0]) == len(client_age)
    if len(client_age) == 1:
        age_cool = not age_cool
    client_age_int = int(client_age)
    if client_age_int < 7:
        result = 'Тебе же {age_part}! Где твои родители?'
    elif client_age_int < 16 and not age_cool:
        result = 'Тебе всего лишь {age_part}, а это фильм для взрослых'
    elif client_age_int > 65 and not age_cool:
        result = 'Вам {age_part}? Покажите пенсионное удостоверение'
    elif age_cool:
        result = 'О, вам {age_part}? Какой интересный возраст!'
    else:
        result = 'Не смотря на то что вам {age_part}, билетов всё равно  нет!'
    return result
    

def age_print_fun(client_age_int, result):
    if 9 < client_age_int < 20:
        age = '{client_age_int} лет'
    else:
        if 4 < client_age_int[-1] < 10 or client_age_int[-1] = 0:
            age = '{client_age_int} лет'
        elif 1 < client_age_int[-1] < 5:
            age = '{client_age_int} года'
        else:
            age = '{client_age_int} год'
    result_str = result.format(age_part=age)

    
client_age = input_fun()
part_1 = logic_fun(client_age)

