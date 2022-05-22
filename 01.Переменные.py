# Python_Hub_Studio
# Python_7_Hours

# ПЕРЕМЕННЫЕ

number = 3 # переменная 1
number2 = 5 # переменная 2
result = number + number2 # сумма переменных
print(result) # OUT: 8

# Каскадное присваивание.
num1 = num2 = 5
print(num1, num2) # OUT: 5 5

# Множественное присвоение.
num_1, num_2 = 5, 7
print(num_1, num_2) # OUT: 5 7

# swap. Обмен данных между переменными
swap1 = 8 # переменная 1
swap2 = 9 # переменная 2
swap1, swap2 = swap2, swap1
print(swap1, swap2) # OUT: 9 8

# обмен данных между переменными с видоизменением одной из переменных (swap2)
swap1 = 8 # переменная 1
swap2 = 9 # переменная 2
swap1, swap2 = swap2, swap1 + swap2
print(swap1, swap2) # OUT: 9 17

# Уменьшение значения переменной 1 на значение переменной 2
swap1 = 8 # переменная 1
number = 4 # переменная 2
# сокращенная запись операции swap1 = swap1 - number
swap1 -= number
print(swap1) # OUT: 4

# Распаковка списка по переменным
x, y, z = [1, 2, 3]
print(x) # OUT: 1
print(y) # OUT: 2
print(z) # OUT: 3

# Распаковка списка по переменным при помощи инструмента arg
x, y, *z = [1, 2, 3, 4, 5]
print(x) # OUT: 1
print(y) # OUT: 2
print(z) # OUT: [3, 4, 5]

# Распаковка списка по переменным при помощи инструмента arg. Второй пример
x, *y, z = [1, 2, 3, 4, 5]
print(x) # OUT: 1
print(y) # OUT: [2, 3, 4]
print(z) # OUT: 5
