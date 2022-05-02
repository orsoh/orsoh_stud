# Hапишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести
#   "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
#
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"
#
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
# Не забувайте що кожна функція має виконувати тільки одну завдання і про правила написання коду.

def input_fun():
    """
    Функция запрашивает у клиента данные о возрасте, проводит валидацию данный и возвращает кортеж
    из данных в формате (str, int)

    :return: кортеж из данных в формате (str, int)
    """
    while True:
        client_age = input('Укажите свой полный возраст ---> ').replace(' ', '').lstrip('0')
        try:
            client_age_int = int(client_age)
            if client_age_int > 130 or client_age_int < 0:
                print('Не верный возраст')
                continue
            break
        except:
            print('Не верный ввод данных')
    return client_age, client_age_int


def msg_part_fun(client_age, client_age_int):
    """
    Функция принимает данные о возрасте клиента и в зависимости от принадлежности возрастному
    отрезку возвращает нужную заготовку сообщения

    :param client_age: данные о возрасте в формате str
    :type client_age: str
    :param client_age_int: данные о возрасте в формате int
    :type client_age_int: int
    :return msg_part: заготовка сообщения в формате str
    """
    age_cool = client_age.count(client_age[0]) == len(client_age)
    if len(client_age) == 1:
        age_cool = not age_cool
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


def age_part_fun(client_age, client_age_int):
    """
    Функция принимает данные о возрасте и после анализа возвращает часть сообщения
    содержащую возраст клиента и слово "год" в нужной форме

    :param client_age: данные о возрасте в формате str
    :type client_age: str
    :param client_age_int: данные о возрасте в формате int
    :type client_age_int: int
    :return age_part: часть сообщения с возрастом клиента в формате str
    """
    if 9 < client_age_int < 20 or 109 < client_age_int < 120:
        age_part = f'{client_age_int} лет'
    else:
        if 4 < int(client_age[-1]) < 10 or int(client_age[-1]) == 0:
            age_part = f'{client_age} лет'
        elif 1 < int(client_age[-1]) < 5:
            age_part = f'{client_age} года'
        else:
            age_part = f'{client_age} год'
    return age_part


def start_all():
    """
    Функция, вызов которой запускает выполнения всего кода,
    формируюет и выводит сообщение ответ
    Всё работает и без неё,
    но "Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг."
    :return:
    """
    client_age_tpl = input_fun()
    msg = msg_part_fun(client_age=client_age_tpl[0], client_age_int=client_age_tpl[1])
    age = age_part_fun(client_age=client_age_tpl[0], client_age_int=client_age_tpl[1])
    res_str = msg.format(age_part=age)
    print(res_str)


start_all()
