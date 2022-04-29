test_list = ('11qwer', 22.2, 33, [4, 44], (5, 55), {6, 66}, {7: 77}, True, None)


def deter_type(test_var):
    result = type(test_var)
    print(result)


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


for test_var in test_list:
    deter_type(test_var)
    
   
for test_var in test_list:
    converter_result = converter_float(test_var)
    print(converter_result)
    
    
result_list = []

for test_var1 in test_list:
    for test_var2 in test_list:
        operation_result = logical_operation(test_var1, test_var2)
        result_list.append(operation_result)
print(result_list)
print(len(result_list))



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
    return client_age_int, result
    

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
    print result_str
    
