# 3.Існує ліст з різними даними,
# наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть механізм, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 3.14, 5.5]
lst2 = []

for element_lst1 in lst1:
    if type(element_lst1) == int or type(element_lst1) == float:
        try:
            lst2.append(element_lst1)
        except Exception as error_list:
            print(f'Я сломался при попытке добавить {element_lst1}')
            print(error_list)
  
print(lst2)
