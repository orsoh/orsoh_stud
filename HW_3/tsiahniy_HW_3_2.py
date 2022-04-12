# 2.Вести з консолі строку зі слів (або скористайтеся константою).
# Напишіть код, який визначить кількість кількість слів, в цмх даних.


new_line = input('Введите строку ---<  ').strip().replace("\n", " ").split(' ')

line_exception0 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '№', '#')
for element0 in line_exception0:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].find(element0) == 0:
            new_line[counter] = new_line[counter][1:]
            continue
        else:
            counter += 1

line_exception1 = ('!', '\"', '.', ',', '?', ':', ';', '\'', '-', '(', ')', '[', ']', '#', '*', '@', '«', '»')

for element1 in line_exception1:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].rfind(element1) == (len(new_line[counter]) - 1):
            new_line[counter] = new_line[counter][:-1]
            continue
        elif new_line[counter].find(element1) == 0:
            new_line[counter] = new_line[counter][1:]
            continue
        else:
            counter += 1

line_exception2 = ('\'', '-')
for element2 in line_exception2:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].find(element2) != -1:
            slice_index = new_line[counter].find(element2)
            new_line[counter] = new_line[counter][:slice_index] + new_line[counter][slice_index + 1:]
            continue
        else:
            counter += 1


counter = new_line.count('')
    
for i in range(counter):
    try:
        new_line.remove('')
    except Exception as error_list:
        print('Я сломался')
        print(error_list)


counter_words = 0
for word in new_line:
    if not word.isalpha():
        print(f'{word} не является словом')
    else:
        counter_words += 1



print(f'Колличество слов: {counter_words}')
