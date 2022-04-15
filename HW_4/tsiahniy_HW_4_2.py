
# Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
# "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких попадають в діапазон між мінімальною і максимальною ціною

shops_dict = {"cito": 47.999,
               "BB_studio": 42.999,
               "momo": 49.999,
               "main-service": 37.245,
               "buy.now": 38.324,
               "x-store": 37.166,
               "the_partner": 38.988,
               "sota": 37.720,
               "rozetka": 38.003}
lower_default = 1000 ** 1000    # Как это можно сделать красивее и менее затратно?
upper_default = 0

for shop in shops_dict.items():
    if shop[1] == '':
        continue
    elif type(shop[1]) == bool:
        print(f'У магазина {shop[0]} цена {shop[1]} указана не верно')
        print('Цена не может быть = bool')
        continue
    try:
        lower_default = shop[1] if lower_default > shop[1] else lower_default
        upper_default= shop[1] if upper_default < shop[1] else upper_default
    except Exception as error_list:
        print(f'У магазина {shop[0]} цена {shop[1]} указана не верно')
        print(error_list)


input_status = False

while not input_status:
    lower_limit = input('Введите нижний ценовой предел ---<  ').strip().replace(',', '.')
    if lower_limit == '':
        lower_limit = lower_default
        input_status = True
        continue
    try:
        lower_limit = float(lower_limit)
        input_status = True
    except Exception as error_list:
        print(f'{lower_limit} не является числом')
        print(error_list)
    if lower_limit < 0:
        input_status = False
        print('Цена должны быть положительным числом')


input_status = False

while not input_status:
    upper_limit = input('Введите верхний ценовой предел ---<  ').strip().replace(',', '.')
    if upper_limit == '':
        upper_limit = upper_default
        input_status = True
        continue
    try:
        upper_limit = float(upper_limit)
        input_status = True
    except Exception as error_list:
        print(f'{upper_limit} не является числом')
        print(error_list)
    if upper_limit <= lower_limit:
        input_status = False
        print('Верхниё предел должен быть больше нижнего')


selectshop_dict = {}

for shop in shops_dict.items():
    if type(shop[1]) == bool:
        continue
    try:
        if lower_limit < shop[1] < upper_limit:
            selectshop_dict[shop[0]] = shop[1]
    except Exception as error_list:
        print('При формировании списка что то пошло не так:')
        print(error_list)
        continue

if len(selectshop_dict) == 0:
    print('Нет магазинов удовлетворяющих требованиям')
else:
    print('Магазины удовлетворяющие требованиям:')
    for shop in selectshop_dict.items():
        print(f'Магазин {shop[0]} цена {shop[1]}')
