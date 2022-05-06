# 1.Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах.
# 2.Напишіть декоратор, який перетворює всі вхідні параметри функції в строки (str)
#   а також перетворює результат роботи функції на строку

import time


def time_calc(fun):
    '''
    Декоратор, выводящий на экран сообщение с временем работы функции в мс
    '''
    def wrapper(*args, **kwargs):
        time_before = time.time()
        res = fun(*args, **kwargs)
        time_after = time.time()
        work_time = (time_after - time_before) * 1000
        print(f'время работы функции {work_time} мс')

        return res

    return wrapper


def change_type(args_type):
    '''
    Декоратор, меняющий тип вводных аргументов и результата работы функции
    если это возможно, если нет оставляет без изменений
    '''
    def first_wrapper(fun):

        def second_wrapper(*args, **kwargs):
            new_args = []
            new_kwargs = {}

            for arg in args:
                if not isinstance(arg, args_type):
                    try:
                        new_arg = args_type(arg)
                        new_args.append(new_arg)
                    except:
                        new_arg = arg
                        new_args.append(new_arg)

            for key, val in kwargs.items():
                if not isinstance(val, args_type):
                    try:
                        new_val = args_type(val)
                        new_kwargs[key] = new_val
                    except:
                        new_val = args_type(val)
                        new_kwargs[key] = new_val
            try:
                result = args_type(fun(*new_args, **new_kwargs))
            except:
                result = fun(*new_args, **new_kwargs)

            return result

        return second_wrapper

    return first_wrapper



def ill_try_faster():
    '''
    Безполезная функция, целью существования которой является загрузить процессор
    :return: всегда возвращает 0
    '''
    zero = 0
    for useless_var in range(4000):
        zero = zero - ((useless_var ** useless_var) - (useless_var ** useless_var))

    return zero


@time_calc
def legendary_fun():
    '''
    Леген... Подожди, подожди... дарно
    :return: возвращает 0 из функции ill_try_faster
    '''
    print('Это было леген...')
    ill_try_faster()
    print('подожди, подожди')
    ill_try_faster()
    print('...дарно')
    result = ill_try_faster()

    return result


@change_type(str)
def levia_fun(century, year):
    '''
    Мифическая функция, вызов которой запускает проверку домашнего задания
    :param century: любые данные в формате строки или числовом
    :param year: любые данные но в том же формате что и century
    :return: возвращает 0 пришедший по эстафете от legendary_fun
    '''
    now = century + year
    print(f'Шел {now} год, но все до сих пор помнят фразу:')
    ill_try_faster()
    zero = legendary_fun()

    return zero


century = 20
#year = 22
work_check = 'А ' + levia_fun(century, year=22) + ' всё ещё равен нулю'
print(work_check)

