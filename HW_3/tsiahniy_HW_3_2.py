# 2.Вести з консолі строку зі слів (або скористайтеся константою).
# Напишіть код, який визначить кількість кількість слів, в цмх даних.
status_line = False

while status_line == False:
    new_line = input('Введите строку ---<  ').strip().split(' ')
    
    counter = new_line.count('')

    for i in range(counter):
        new_line.remove('')
        
    status_line = True
    for word in new_line:
        if not word.isalpha():
            print(f'{word} is not word')
            status_line = False
        
            
print(new_line)
