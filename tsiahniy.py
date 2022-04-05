#1  Задача: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

print('')

first = 10
second = 30

print(first + second)
print(first - second)
print(first * second)
print(first / second)
print(first ** second)
print('')

#2  Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
#Виведіть на екран результат кожного порівняння.

result_bool = True

result_bool = first < second
print(result_bool)

result_bool = first <= second
print(result_bool)

result_bool = first > second
print(result_bool)

result_bool = first >= second
print(result_bool)

result_bool = first == second
print(result_bool)

result_bool = first != second
print(result_bool)

print('')

#3  Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
# Виведіть на екран.

result_str = ''
str1 = 'Hello '
str2 = 'world'

# способ 1
result_str = str1 + str2
print(result_str)

# способ 2
tpl = '%s%s'
result_str = tpl % (str1 , str2)
print(result_str)

# способ 3.1
tpl = '{}{}'
result_str = tpl.format(str1, str2)
print(result_str)

# способ 3.2
tpl = '{part_1}{part_2}'
result_str = tpl.format(part_1=str1, part_2=str2)
print(result_str)

# способ 4
result_str = f'{str1}{str2}'
print(result_str)