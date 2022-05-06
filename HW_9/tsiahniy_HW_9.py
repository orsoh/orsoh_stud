
import time


def time_calc(fun):
    def wrapper(*args, **kwargs):
        time_before = time.time()
        res = fun(*args, **kwargs)
        time_after = time.time()
        work_time = (time_after - time_before) * 1000
        print(f'время работы функции {work_time} мс')

        return res

    return wrapper


def change_type(args_type):
    def first_wrapper(fun):
        def second_wrapper(*args, **kwargs):
            new_args = []
            new_kwargs = {}
            for arg in args:
                if not isinstance(arg, args_type):
                    new_arg = args_type(arg)
                    new_args.append(new_arg)
            for key, val in kwargs.items():
                if not isinstance(val, args_type):
                    new_val = args_type(val)
                    new_kwargs[key] = new_val

            result = args_type(fun(*new_args, **new_kwargs))
            return result
        return second_wrapper
    return first_wrapper



def ill_try_faster():
    for useless_var in range(4000):
        zero = (useless_var ** useless_var) - (useless_var ** useless_var)
    return zero


@time_calc
def legendary_fun():
    print('Это было леген...')
    ill_try_faster()
    print('подожди, подожди')
    ill_try_faster()
    print('...дарно')
    result = ill_try_faster()
    return result


@change_type(str)
def levia_fun(century, year):
    now = century + year
    print(f'Шел {now} год, но все до сих пор помнят фразу:')
    ill_try_faster()
    zero = legendary_fun()
    return zero


#century = 20
#year = 22
work_check = 'А ' + levia_fun(century=20, year=22) + ' всё ещё равен нулю'
print(work_check)

