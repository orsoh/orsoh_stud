client_age = ''
while not client_age.isdigit():
    client_age = input('Укажите свой полный возраст ---> ').replace(' ', '')
    if len(client_age) > 1:
        client_age.lstrip('0')
    if not client_age.isdigit():
        print('Не верный ввод данных')
    elif int(client_age) > 130:
        client_age = ''
        print('Не верный возраст')
client_age_int = int(client_age)
massiv = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
counter = 0

while not counter == 10:
    try:
        k = 1 / (client_age_int - massiv[counter])
        counter = counter +1
    except ZeroDivisionError:
        k = 0
        print('Какой интересный возраст!')
        counter = 10
        exit()

print('Кyjhv')


