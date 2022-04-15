new_line = input('Введите строку ---<  ').strip().replace('/', ' ').split(' ')

line_exception0 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '№', '#')

for element0 in line_exception0:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].find(element0) == 0:
            try:
                new_line[counter] = new_line[counter][1:]
            except Exception as error_list:
                print(f'Я сломался при попытке убрать {element0} с начала {new_line[counter]}')
                print(error_list)
                counter += 1
            continue
        else:
            counter += 1

import string

line_exception1 = string.punctuation

for element1 in line_exception1:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].rfind(element1) == (len(new_line[counter]) - 1):
            try:
                new_line[counter] = new_line[counter][:-1]
            except Exception as error_list:
                print(f'Я сломался при попытке убрать {element1} с конца {new_line[counter]}')
                print(error_list)
                counter += 1
            continue
        elif new_line[counter].find(element1) == 0:
            try:
                new_line[counter] = new_line[counter][1:]
            except Exception as error_list:
                print(f'Я сломался при попытке убрать {element1} с начала {new_line[counter]}')
                print(error_list)
                counter += 1
            continue
        else:
            counter += 1

line_exception2 = ('\'', '-', '–')

for element2 in line_exception2:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].find(element2) != -1:
            slice_index = new_line[counter].find(element2)
            try:
                new_line[counter] = new_line[counter][:slice_index] + new_line[counter][slice_index + 1:]
            except Exception as error_list:
                print(f'Я сломался при попытке убрать {element2} из середины {new_line[counter]}')
                print(error_list)
                counter += 1
            continue
        else:
            counter += 1

counter = new_line.count('')

for i in range(counter):
    try:
        new_line.remove('')
    except Exception as error_list:
        print('Я сломался при попытке убрать пустые ячейки')
        print(error_list)

words_list = []
counter_words = 0

for word in new_line:
    if not word.isalpha():
        print(f'{word} не является словом')
    else:
        counter_let = 0
        letters_dict = {}
        word = word.lower()
        for let in word:
            letters_dict.update({counter_let: let})
            counter_let += 1
        counter_words += 1
        words_list.append(letters_dict)
print(words_list)

exception_letters = ('e', 'y', 'u', 'i', 'o', 'a', 'е', 'а', 'о', 'э', 'я', 'и', 'у', 'ы', 'ё', 'ю')
newwords_list = {}

counter_words = 0
for word in words_list:
    counter_let = 0
    for key, let in word.items():
        for element4 in exception_letters:
            if let.find(element4) != -1:
                print('lol')
                print(counter_words)
                print(key)
                print(let)
                # newwords_list[counter_words].update(key: let)
        #       counter_let += 1
        #   else:
        #       counter_let += 1
    counter_words += 1
print(newwords_list)
print(f'Колличество слов: {counter_words}')