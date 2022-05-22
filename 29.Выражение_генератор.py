# Python_Hub_Studio
# Python_7_Hours

from rich import print

# ВЫРАЖЕНИЕ ГЕНЕРАТОР. (...) VS [...]


# ГЕНЕРАТОР СПИСКОВ [...]
my_path = 'path_to_files'
my_list = [
    my_path+'Example_calc.exe',
    my_path+'File1.txt',
    my_path+'File2.txt',
    my_path+'File3.bmp',
    my_path+'File4.txt',
    my_path+'File5.bmp',
    my_path+'New_file1.txt',
    my_path+'New_file2.txt',
    my_path+'New_file3.txt',
    my_path+'New_file4.txt'
]
# print(my_list) # раскоментировать для просмотра

# n - генератор списка
# разобьем список my_list по разделителю, срежем часть пути до файла и создадим новый список из имен файлов, имеющих
# расширение .txt
n = [i.split(my_path)[1]
for i in my_list if ".txt" in i]

print(n) # OUT: ['File1.txt', 'File2.txt', 'File4.txt', 'New_file1.txt', 'New_file2.txt', 'New_file3.txt', 'New_file4.txt']
print(type(n)) # OUT: <class 'list'>
# !!! СПИСОК, созданный генератором списков хранится в памяти программы и занимает большое количество памяти ПК !!!

# Поскольку n является списком, мы МОЖЕМ запрашивать информацию из него по индексу.
print(n[1]) # OUT: New_file2.txt


# ВЫРАЖЕНИЕ ГЕНЕРАТОР (...)
my_path = 'path_to_files'
my_list = [
    my_path+'Example_calc.exe',
    my_path+'File1.txt',
    my_path+'File2.txt',
    my_path+'File3.bmp',
    my_path+'File4.txt',
    my_path+'File5.bmp',
    my_path+'New_file1.txt',
    my_path+'New_file2.txt',
    my_path+'New_file3.txt',
    my_path+'New_file4.txt'
]
# print(my_list) # раскоментировать для просмотра

# m - выражение генератор
# разобьем список my_list по разделителю, срежем часть пути до файла и создадим новый список из имен файлов, имеющих
# расширение .txt
m = (i.split(my_path)[1]
for i in my_list if ".txt" in i)

print(m) # OUT: <generator object <genexpr> at 0x000000000370BD60>
print(type(m)) # OUT: <class 'generator'>

# итерация по элементам
# for i in m:
#    print(i)
'''OUT:
File1.txt
File2.txt
File4.txt
New_file1.txt
New_file2.txt
New_file3.txt
New_file4.txt
'''

# Поскольку выражение-генератор не является списком, НЕЛЬЗЯ запрашивать информацию из него по индексу.
# print(m[1]) # OUT: TypeError: 'generator' object is not subscriptable

# Функция next(), позволяет запрашивать информацию аналогично запросу к списку по индексу.
print(next(m)) # OUT: New_file.txt


# ТЕСТ НА ЗАТРАТЫ ВРЕМЕНИ И ПАМЯТИ. (...) VS [...]
import os
import time


# ГЕНЕРАТОР списка

# ВРЕМЕНИ на парсинг ВСЕГО диска "C" при помощи генератора списков уходит ОЧЕНЬ МНОГО.
# РЕСУРСОВ ПК для хранения информации в переменной 'n' так же нужно ОЧЕНЬ МНОГО.
start = time.time()
n = [i for i in os.walk("C:\\")]
finish = time.time() - start

print(finish) # OUT: 3.2904000282287598      # ВРЕМЯ
print(n.__sizeof__()) # OUT: 253608          # ПАМЯТЬ


# выражение ГЕНЕРАТОР

# ВРЕМЕНИ на парсинг ВСЕГО диска "C" при помощи выражения-генератора равно НУЛЮ.
# РЕСУРСОВ ПК для хранения информации в переменной m практически НЕ НУЖНО.
start2 = time.time()
m = (j for j in os.walk("C:\\"))
finish2 = time.time() - start2

print(finish2) # OUT: 0.0                    # ВРЕМЯ
print(m.__sizeof__()) # OUT: 96              # ПАМЯТЬ
