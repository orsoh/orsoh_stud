# 1.Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
#Наприклад "The [значення нокра символа] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

new_word = ''
new_number = ''

while not new_word.isalpha() or not len(new_word) > 0:
    new_word = input('Введите слово ---> ').replace(' ', '')

    if not new_word.isalpha():
        print('Данные не являются словом')

   
print(f'Вы ввели слово {new_word}')


while not new_number.isdigit():
    new_number = input(f'Введите число 1 до {len(new_word)} ---> ').replace(' ', '')
    
    if not new_number.isdigit():
        print('Данные не являются числом')
        new_number = ''
    elif int(new_number) > len(new_word):
        print('Число слишком большое')
        new_number = ''
    elif int(new_number) == 0:
        print('Число не должно быть равно нулю')
        new_number = ''

   
print(f'Вы ввели число {new_number}')

print(f'В слове {new_word} символ под номером {new_number} это {new_word[int(new_number)-1]}')
