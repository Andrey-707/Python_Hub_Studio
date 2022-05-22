# Python_Hub_Studio
# Python_7_Hours

# ПАРСЕР ФАЙЛОВ.

# Пример_1.
'''
У нас есть главная директория, путь до которой мы передаём в 'path'. В этой директории лежит ещё две директории
'Dir_1', 'Dir_2' и ещё несколько файлов ('Example_calc.exe', 'File1.txt', 'File2.txt', 'File3.bmp',
'New_file1.txt', 'New_file2.txt', 'New_file3.txt', 'New_file4.txt'). В директории 'Dir_1' находится два файла
('File4.txt', 'File5.bmp'). Используем модуль 'os' для получения данных.

Функция .walk() модуля 'os' выдает кортеж из трех элементов:
1. Строка, которую мы передали (path)
2. Список с именами папок, которые находятся по адресу (path)
3. Список с именами файлов, которые находятся по адресу (path)
!!! Далее с помощью цикла for происходит углубление в папки.
'''
import os

from rich import print # визуализицая выходных данных


# directory_path
path = "your_directory_path\\12.Files_Parser"

# функция .walk() - функция-генератор
for i in os.walk(path):
    print(i)
# OUT:
'''
(
    'your_directory_path\\12.Files_Parser',
    ['Dir_1', 'Dir_2'],
    [
        'Example_calc.exe',
        'File1.txt',
        'File2.txt',
        'File3.bmp',
        'New_file1.txt',
        'New_file2.txt',
        'New_file3.txt',
        'New_file4.txt'
    ]
)
('your_directory_path\\Dir_1', [], ['File4.txt', 'File5.bmp'])
('your_directory_path\\Dir_2', [], [])
'''


# Пример_2.
# функция .walk() выдает список с адресами ко ВСЕМ файлам
import os

from rich import print # визуализицая выходных данных


# directory_path
path = "your_directory_path\\12.Files_Parser"
some_list = []

# функция .walk() - функция-генератор
for adress, dirs, files in os.walk(path):
    for file in files:
        # функция os.path.join() объединяет пути с особенностями системы (проставтяет слэши)
        some_list.append(os.path.join(adress, file))
else:
    print(some_list)
# OUT:
'''
[
    'your_directory_path\\12.Files_Parser\\Example_calc.exe',
    'your_directory_path\\12.Files_Parser\\File1.txt',
    'your_directory_path\\12.Files_Parser\\File2.txt',
    'your_directory_path\\12.Files_Parser\\File3.bmp',
    'your_directory_path\\12.Files_Parser\\New_file1.txt',
    'your_directory_path\\12.Files_Parser\\New_file2.txt',
    'your_directory_path\\12.Files_Parser\\New_file3.txt',
    'your_directory_path\\12.Files_Parser\\New_file4.txt',
    'your_directory_path\\12.Files_Parser\\Dir_1\\File4.txt',
    'your_directory_path\\12.Files_Parser\\Dir_1\\File5.bmp'
]
'''


# Пример_3.
# функция .walk() выдает список с адресами к файлам 
# с помощью условия if применен фильтр для файлов с расширением .txt
import os

from rich import print


# directory_path
path = "your_directory_path\\12.Files_Parser"
some_list = []

# функция .walk() - функция-генератор
for adress, dirs, files in os.walk(path):
    for file in files:
        # функция os.path.join() объединяет пути с особенностями системы (проставтяет слэши)
        full = os.path.join(adress, file)
        if '.txt' in full:
            some_list.append(full)
else:
    print(some_list)
# OUT:
'''
[
    'your_directory_path\\12.Files_Parser\\File1.txt',
    'your_directory_path\\12.Files_Parser\\File2.txt',
    'your_directory_path\\12.Files_Parser\\New_file1.txt',
    'your_directory_path\\12.Files_Parser\\New_file2.txt',
    'your_directory_path\\12.Files_Parser\\New_file3.txt',
    'your_directory_path\\12.Files_Parser\\New_file4.txt',
    'your_directory_path\\12.Files_Parser\\Dir_1\\File4.txt'
]
'''


# Пример_4.
# функция .walk() выдает список с адресами к файлам
# с помощью условия if применим фильтр для созданных файлов, которые были созданы
# сегодня (время создания менее суток).
import os
import time

from rich import print


# directory_path
path = "your_directory_path\\12.Files_Parser"
some_list = []

# функция .walk() - функция-генератор
for adress, dirs, files in os.walk(path):
    for file in files:
        # функция os.path.join() объединяет пути с особенностями системы (проставтяет слэши)
        full = os.path.join(adress, file)
        # time.time() - текущее время с момента начала эпохи
        # os.path.getctime(full) - время создания файла с начала эпохи
        # разница 86400 сек - это сутки
        if time.time() - os.path.getctime(full) < 86400:
            some_list.append(full)
else:
    print(some_list)
# OUT:
'''
[
    'your_directory_path\\12.Files_Parser\\Example_calc.exe',
    'your_directory_path\\12.Files_Parser\\File1.txt',
    'your_directory_path\\12.Files_Parser\\File2.txt',
    'your_directory_path\\12.Files_Parser\\File3.bmp',
    'your_directory_path\\12.Files_Parser\\New_file1.txt',
    'your_directory_path\\12.Files_Parser\\New_file2.txt',
    'your_directory_path\\12.Files_Parser\\New_file3.txt',
    'your_directory_path\\12.Files_Parser\\New_file4.txt',
    'your_directory_path\\12.Files_Parser\\Dir_1\\File4.txt',
    'your_directory_path\\12.Files_Parser\\Dir_1\\File5.bmp'
]
'''
