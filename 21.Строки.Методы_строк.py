# Python_Hub_Studio
# Python_7_Hours

# СТРОКИ. МЕТОДЫ СТРОК.

# Индексы элементов строки
# индекс                    0123
# string =                 "stroka teksta"
# отрицательный индекс                 -1

# Вывод элемента по индексу
s = "stroka teksta"
print(s[2]) # OUT: r

# Срез строки. s[start:stop:step]
s = "stroka teksta"
print(s[0:5]) # OUT: strok

# Строка и подстрока.
s = "stroka teksta"
ss = "str"
print(ss in s) # OUT: True

# Строка и подстрока.
s = "stroka teksta"
ss = "sto"
print(ss in s) # OUT: False


# МЕТОДЫ СТРОК.

# Метод .upper() переводит ВСЕ символы строки в верхний регистр
# Метод НЕ изменяет строку, а возвращает значение, которое можно присвоить переменной.
s = "stroka teksta"
print(s.upper()) # OUT: STROKA TEKSTA

# Метод .lower() переводит ВСЕ символы строки в нижний регистр
# Метод НЕ изменяет строку, а возвращает значение, которое можно присвоить переменной.
s = "STROKA TEKSTA"
print(s.lower()) # OUT: stroka teksta

# Метод .capitalize() переводит ПЕРВЫЙ символ строки в верхний регистр, а остальные символы строки в нижний.
# Метод НЕ изменяет строку, а возвращает значение, которое можно присвоить переменной.
s = "STROKA TEKSTA"
print(s.capitalize()) # OUT: Stroka teksta

# Метод .replace() позволяет заменить символ на другой. Поменять слэш в строке прямой на обратный
path = r"D:/path_to_file/File.txt"
new_path = path.replace("/", "\\")
print(path) # OUT: D:/path_to_file/File.txt
print(new_path) # OUT: D:\path_to_file\File.txt

# Метод .split("/") позволяет разделить строку и отобразить в виде списка. Символ-разделитель задается
# в скобках .split("/")
path = "D:/Dir_Name/01.Переменные.py"
new_path = path.split("")
print(path) # OUT: D:/Dir_Name/01.Переменные.py
print(new_path) # OUT: ['D:', 'Dir_Name', '01.Переменные.py']

# Разделив строку, можем вывести на экран имя файла
path = "D:/Dir_Name/01.Переменные.py"
new_path = path.split("/")
print(path) # OUT: D:/Dir_Name/01.Переменные.py
print(new_path[-1]) # OUT: 01.Переменные.py

# Метод .split("\\") позволяет разделить строку и отобразить в виде списка. Символ-разделитель задается
# в скобках .split("\\"). Символа-разделителя НЕТ (не подходит), метод возвращает один элемент.
path = "D:/Dir_Name/01.Переменные.py"
new_path = path.split("\\")
print(path) # OUT: D:/Dir_Name/01.Переменные.py
print(new_path) # OUT: ['D:/Dir_Name/01.Переменные.py']

# Символ-разделитель НЕ ПРОПИСАН .split(""), метод выдает ошибку ValueError. ДО ВЫВОДА print(path)
path = "D:/Dir_Name/01.Переменные.py"
new_path = path.split("")
# ПРОГРАММА ВЫЛЕТАЕТ РАНЬШЕ вызова print()
# OUT: ValueError: empty separator
print(path)
print(new_path)

# Символ-разделитель ПРОПИСАН как пробел .split(" "), в данном случае метод работает
path = "D:/Dir_Name/01. Переменные.py"
new_path = path.split(" ")
print(path) # OUT: D:/Dir_Name/01.Переменные.py
print(new_path) # OUT: ['D:/Dir_Name/01.', 'Переменные.py']

# ЗАДАЧА
# Обработать текст. Выполнить требования, которые прописаны в тексте, т.е. сделать единую строку.
# Оригинальный текст сохранен в файле 21.String.txt
import random

from rich import print
from rich.progress import track
from time import sleep
from time import time


print("[bold magenta]Program start[/]")

# запуск счетчика
start = time()

# Обрабатываем текст-копию 21.String_copy.txt
# открыть текстовый файл

text_c = open(r"path_to_file\21.String_copy.txt")

# прочитать текстовый файл
r = text_c.read()

# вывод результата
print("[bold cyan]Шаг_1. Считываем файл-копию 21.String_copy.txt[/]")
print(r)

# Progress-bar
def do_step(step):
    sleep(random.uniform(0.01, 0.1))

print("[bold cyan]Шаг_2. Выполнение программы[/]")
for step in track(range(100), description="Обработка файла..."):
    do_step(step)

# список символов, которые нужно удалять из текста
list_symbol = ["(", ")", "'", "\"", "\n"]

# итерация списка символов
for i in list_symbol:
    # замена в тексте символа из списка list_symbol на ПУСТОТУ, т.е. удаление
    r = r.replace(i, "")

# вывод результата
print("[bold cyan]Шаг_3. Удаление символов[/]")
print(r)
sleep(1)

# разбить строку по разделителю "пробел", используя метод .split()
r1 = r.split()

# вывод результата
print("[bold cyan]Шаг_4. Разделение строки[/]")
print(r1)
sleep(1)

# объединить обратно, используя метод .join(). В него передаем список. Спереди указать чем заполнить пробелы
text_new = "_".join(r1)

# вывод результата
print("[bold cyan]Шаг_5. Обьединение в строку[/]")
print(text_new)
sleep(1)

# Запишем текст, используя кодировку "utf-8"
ttext = open(r"path_to_file\21.String_done.txt",
    "w", encoding="utf-8") # такого файла нет, поэтому он создается "w", кодировка utf-8)
ttext.write(text_new)

# закрыть текстовый файл
text_c.close() # закрыть файл
ttext.close() # закрыть файл

# Время выполнени программы
print("[bold cyan]Шаг_6. Результат[/]")
print("Затреченное время составило {:.2F}".format(time() - start), "сек")

print("[bold magenta]Program finish[/]")
