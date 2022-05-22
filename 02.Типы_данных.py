# Python_Hub_Studio
# Python_7_Hours

# ТИПЫ ДАННЫХ

# Python - язык с диномической типизацие данных, поэтому можно присвоить и переприсвоить любой
# тип данных в одну и ту же переменную (например, в переменную "a")

# НЕТ данных
a = None
print(type(a)) # OUT: <class 'NoneType'>

# целое число
a = 1
print(type(a)) # OUT: <class 'int'>

# число с плавающей точкой
a = 1.0
print(type(a)) # OUT: <class 'float'>

# комплексное число
a = 1 + 1j
print(a) # OUT: (1+1j)
print(type(a)) # OUT: <class 'complex'>

# строка
a = "1"
print(type(a)) # OUT: <class 'str'>

# список
a = [1, 1, "1"]
print(type(a)) # OUT: <class 'list'>

# кортеж
a = (1, 1, "1")
print(type(a)) # OUT: <class 'tuple'>

# множество
a = {1, 2, "a"}
print(type(a)) # OUT: <class 'set'>

# словарь
a = {"a":1, "b":2}
print(type(a)) # OUT: <class 'dict'>

# логическое (булево) значение
a = True # или False
print(type(a)) # OUT: <class 'bool'>


# Целые числа <class 'int'> и числа с плавающей точкой <class 'float'> поддерживают любые
# математические операции.

a = 5 + 5
print(a) # OUT: 10

a = 5.0 + 5
print(a) # OUT: 10.0

# Объединение строк (конкатенация)
a = "string" + "12345"
print(a) # OUT: string12345

# Объединение строк (конкатенация) с конвертированием данных
a = "string" + str(12345)
print(a) # OUT: string12345

# При помощи встроенной функции "input()" можно ввести значение и при помощи встроенной функции "type()"
# можно узнать тип введенного значения.

x = input("Ввод: ") # введем число 123
# с клавиатуры вводится СТРОКА (тип данных str) !!!
print(x) # OUT: 123
print(type(x)) # OUT: <class 'str'>

# конвертирование введенных данных с клавиатуры в целое число
r = 5 + int(x)
print(r) # OUT: 128
print(type(r)) # OUT: <class 'int'>

# конвертирование данных на ввод и вывод
x = float(input("Введите первое число: ")) # 5
y = float(input("Введите второе число: ")) # 6
r = x + y
print("Результат: " + str(r)) # OUT: Результат: 11.0
