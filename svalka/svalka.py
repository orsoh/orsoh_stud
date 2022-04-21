shops_dict = {"cito": 47.999,
               "BB_studio": 42.999,
               "momo": 49.999,
               "main-service": 37.245,
               "buy.now": 38.324,
               "x-store": 37.166,
               "the_partner": 38.988,
               "sota": 37.720,
               "rozetka": 38.003}

low_limit = float(input('low'))
upper_limit = float(input('up'))

new_dict = {}

for brand, price in shops_dict.items():
    if low_limit < price < upper_limit:
        new_dict[brand] = price

print(new_dict)