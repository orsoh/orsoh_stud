# 1.Напишіть функцію, що приймає один аргумант. Функція має вивести на ектан тип цього аргумента (використовуйте type)
# 2.Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
#   Якщо перетворити не вдається функція має повернути 0.
# 3.Напишіть функцію, що приймає два аргументи. Функція повинна
#   a) якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
#   b) якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
#   c) якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
#   d) у будь-якому іншому випадку повернути кортеж з цих аргументів

test_list = ('11qwer', 22.2, 33, [4, 44], (5, 55), {6, 66}, {7: 77}, True, None)


def deter_type(test_var):
    result = type(test_var)
    print(f'{test_var} is {result}')


def converter_float(test_var):
    try:
        result = float(test_var)
    except:
        result = 0
    return result


def logical_operation(test_var1, test_var2):
    cond1 = isinstance(test_var1, int) or isinstance(test_var1, float)
    cond2 = isinstance(test_var2, int) or isinstance(test_var2, float)
    if cond1 and cond2:
        result = test_var1 - test_var2
    elif isinstance(test_var1, str) and isinstance(test_var2, str):
        result = test_var1 + test_var2
    elif isinstance(test_var1, str) and not isinstance(test_var2, str):
        result = {test_var1: test_var2}
    else:
        result = (test_var1, test_var2)
    return result


# Ниже проверка на работоспособность функций


for test_var in test_list:
    deter_type(test_var)

for test_var in test_list:
    converter_result = converter_float(test_var)
    print(converter_result)

result_list = []

# Прогоняем все возможные комбинации типов данных

for test_var1 in test_list:
    for test_var2 in test_list:
        operation_result = logical_operation(test_var1, test_var2)
        result_list.append(operation_result)
print(result_list)
print(len(result_list))
