# 2.Вести з консолі строку зі слів (або скористайтеся константою).
# Напишіть код, який визначить кількість кількість слів, в цмх даних.
status_line = False

while status_line == False:
    status_line = True
    new_line = input('Введите строку ---<  ').strip().split(' ')
    
    counter = new_line.count('')
    
    for i in range(counter):
        try:
            new_line.remove('')
        except Exception as error_list:
            print('Я сломался')
            print(error_list)
            status_line = False
            
    for word in new_line:
        if not word.isalpha():
            print(f'{word} не является словом')
            status_line = False
        

counter_word = len(new_line)

print(f'Колличество слов: {counter_word}')
