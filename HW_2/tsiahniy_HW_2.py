#Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#Попросіть користувача ввести свсвій вік (можно використати константу або input()).
#- якщо користувачу менше 7 - вивести "Де твої батьки?"
#- якщо користувачу менше 16 - вивести "Це фільм для дорослих!"
#- якщо користувачу більше 65 - вивести "Покажіть пенсійне посвідчення!"
#- якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років) - вивести "Який цікавий вік!"
#- у будь-якому іншому випадку - вивести "А білетів вже немає!"

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

age_cool = client_age.count(client_age[0]) == len(client_age)
if len(client_age) == 1:
    age_cool = not age_cool

client_age_int = int(client_age)
if client_age_int < 7:
    print('Где твои родители?')
elif client_age_int < 16 and not age_cool:
    print('Это фильм для взрослых')
elif client_age_int > 65 and not age_cool:
    print('Покажите пенсионное удостоверение')
elif age_cool:
    print('Какой интересный возраст!')
else:
    print('А билетов уже нет!')


#СТАРЫЙ КОД
#    age = input('Укажите свой полный возраст')
#    age = age.replace(' ', '')
#    age = age.lstrip('0')
#
#    if age.isdigit() == True:
#        age = int(age)
#    else:
#        print('Не верный возраст')
#        exit()
#
#    age_str = str(age)
#    counter = len(age_str) - 1
#    if counter > 0:
#        while counter > 0:
#            if int(age_str[counter]) == int(age_str[counter - 1]):  # последовательно сравниваю
#                counter -= 1  # значения от последнего до нулевого индекса
#            else:
#                break
#        if counter == 0:
#            print('Какой интересный возраст!')
#
#    if age <= 7:
#        print('Где твои родители?')
#    elif 7 < age <= 16:
#       print('Покажите пенсионное удостоверение')
#    else:
#        print('А билетов уже нет!')





