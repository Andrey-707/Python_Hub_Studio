# Python_Hub_Studio
# Python_7_Hours

# КОРТЕЖИ
# !!! КОРТЕЖИ ОТНОСЯТСЯ К НЕИЗМЕНЯЕМЫМ ТИПАМ ДАННЫХ !!!

some_tuple = () # можно записывать БЕЗ скобок x = 9, 8, 7, 6
print(type(some_tuple)) # OUT: <class 'tuple'>

some_tuple = (9, 8, 7, 6, 5, 4)
# index       0  1  2  3  4  5

# выведем на печать элемент кортежа с индексом 3
print(some_tuple[3]) # OUT: 6

# узнать длину кортежа можно, вызвав функцию len()
print(len(some_tuple)) # OUT: 6

# выведем на печать последний элемент кортежа (не важно какой у него порядковый номер)
# для этого применим отрицательный индекс кортежа -1
print(some_tuple[-1]) # OUT: 4

# КОРТЕЖИ могут содержать числа,
some_tuple = (9, 8, 7, 6, 5, 4)
print(some_tuple) # OUT: (9, 8, 7, 6, 5, 4)

# буквы (строки),
some_tuple = (9, 8, 7, 6, 5, 4, 'a')
print(some_tuple) # OUT: (9, 8, 7, 6, 5, 4, 'a')

# списки (вложенные сиски),
some_tuple = (9, 8, 7, 6, 5, 4, 'a', [1, 2, 3])
print(some_tuple) # OUT: (9, 8, 7, 6, 5, 4, 'a', [1, 2, 3])

# Последним элемент кортежа сейчас является вложенный список.
# выведем на печать последний элемент этого вложенного списка.
print(some_tuple[-1][-1]) # OUT: 3

# Поскольку КОРТЕЖИ являются НЕизменяемым типом данных, НЕЛЬЗЯ заменить индекс (элемент) кортежа.
some_tuple = (9, 8, 7, 6, 5, 4)
some_tuple[0] = 10
print(some_tuple[0]) # OUT: TypeError: 'tuple' object does not support item assignment

# НЕЛЬЗЯ заменить индексы (элементы) в кортеже друг на друга. НЕЛЬЗЯ сделать 'swap'
some_tuple = (9, 8, 7, 6, 5, 4)
# index       0  1  2  3  4  5
print(some_tuple) # OUT: (9, 8, 7, 6, 5, 4)
some_tuple[2], some_tuple[3] = some_tuple[3], some_tuple[2]
print(some_tuple) # OUT: TypeError: 'tuple' object does not support item assignment

# Можно вывести значения кортежа по переменным.
some_tuple = (9, 8, 7)
x, y, z = some_tuple
print(x) # OUT: 9
print(y) # OUT: 8
print(z) # OUT: 7

# Если вывести значения кортежа по переменным, то данный случай приведет к ошибке.
some_tuple = (9, 8, 7, 6)
x, y, z = some_tuple
# OUT: ValueError: too many values to unpack (expected 3)
print(x)
print(y)
print(z)
# Для устранения ошибки нужно добавить ещё одну переменную w, x, y, z = some_tuple

# Метод ОБМЕНА данными между переменными.
some_tuple = (9, 8, 7, 6, 5, 4)
# index       0  1  2  3  4  5
a = 5
b = 6
a, b = b, a
# на основании данного метода сделаем срез кортежа. Срезается start с индекса 1 по индекс 4 stop НЕ ВКЛЮЧИТЕЛЬНО
some_tuple[1:4]
print(some_tuple[1:4]) # OUT: (8, 7, 6)

# Можно добавлять элементы к кортежу. Добавим цифру 3 к кортежу.
# Этот метод является склеиванием двух кортежей (9, 8, 7, 6, 5, 4) и (3,)
some_tuple = (9, 8, 7, 6, 5, 4)
print(some_tuple) # OUT: ((9, 8, 7, 6, 5, 4)
# some_tuple = some_tuple + 3 # TypeError: can only concatenate tuple (not "int") to tuple
# some_tuple = some_tuple + (3) # TypeError: can only concatenate tuple (not "int") to tuple
some_tuple = some_tuple + (3,) # такой случай не вызывает ошибку
print(some_tuple) # OUT: (9, 8, 7, 6, 5, 4, 3)

# КОРТЕЖИ можно продублировать, применив умножение.
some_tuple = (1, 2, 3)
print(some_tuple) # OUT: (1, 2, 3)
some_tuple = some_tuple*2
print(some_tuple) # OUT: (1, 2, 3, 1, 2, 3)

# Можно СОЗДАВАТЬ КОРТЕЖИ из строк. Сконвертировать строку в КОРТЕЖ.
# Для этого используется функция tuple()
x = tuple("string")
print(x) # OUT: ('s', 't', 'r', 'i', 'n', 'g')

# Можно СОЗДАВАТЬ КОРТЕЖИ из последовательности чисел.
some_tuple = tuple(range(11))
print(some_tuple) # OUT: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# КОРТЕЖИ можно итерировать, обходя по элементам при помощи цикла.
some_tuple = tuple(range(1, 6))
print(some_tuple) # OUT: (1, 2, 3, 4, 5)
for i in some_tuple:
	print(i) # выводит каждую итерацию по одному элементу кортежа от 1 до 5

# Имея КОРТЕЖ, изменить значение индексов СПИСКА на фиксированное значение a = 3.
some_tuple = (9, 8, 7, 6, 5, 4)
some_list = []
a = 3
for i in range(len(some_tuple)):
    # данный метод не вызывает ошибку, поскольку мы НЕ ПРИСВАИВАЕМ ЗНАЧЕНИЯ
    # элементам кортежа
    some_list.append(some_tuple[i] + a)
print(some_list) # OUT: [12, 11, 10, 9, 8, 7]

# <<Изменить кортеж>>.
# Увеличим значение индексов (элементов) кортежа на фиксированное значение a = 3.
# Т.к. КОРТЕЖИ являются НЕизменяемым типом данных используем конвертацию в список и обратно.
some_tuple = (9, 8, 7, 6, 5, 4)
a = 3
some_list = list(some_tuple)
for i in range(len(some_list)):
	some_list[i] += a

some_tuple = tuple(some_list)
print(some_tuple) # OUT: (12, 11, 10, 9, 8, 7)


# МЕТОДЫ КОРТЕЖЕЙ. Их два.

# Метод .count() позволяет посмотреть сколько раз повторяется число 9 в кортеже
some_tuple = (9, 8, 7, 6, 5, 9)
print(some_tuple.count(9)) # OUT: 2

# Метод .index() позволяет посмотреть какой индекс у числа 9. Слева направо.
some_tuple = (9, 8, 7, 6, 5, 9)
print(some_tuple.index(9)) # OUT: 0 

# Копирование кортежей.
some_tuple1 = (9, 8, 7, 6)
some_tuple2 = some_tuple1
# Поскольку кортеж является неизменяемым типом данных, если мы изменяем кортеж'some_tuple1' конкатенацией
# кортежей, то кортеж 'some_tuple2' при этом не изменяется.
some_tuple1 += (5, 4)
print(some_tuple1) # OUT: (9, 8, 7, 6, 5, 4)
print(some_tuple2) # OUT: (9, 8, 7, 6)
