# Python_Hub_Studio
# Python_7_Hours

# ОБРАБОТКА ИСКЛЮЧЕНИЙ

# пользователь передает НЕ число, программа крашится с ошибкой ValueError
enter = float(input("Введите число: "))
# OUT: ValueError: could not convert string to float: 'g'

# Обработка исключений. Операторы 'try' и 'except'.
try:
	enter = float(input("Введите число: "))
except ValueError:
	print("ValueError. Вы ввели не число")

# Обработка исключений и повторный запрос.
# при повторной попытке пользователя передать НЕ число, программа крашится с ошибкой ValueError
try:
    enter = float(input("Введите число: "))
except ValueError:
    print("ValueError. Вы ввели не число. Повторите ввод")
    enter = float(input("Введите число: "))
# OUT: ValueError: could not convert string to float: 'h'

# Обработка исключений в бесконечном цикле.
# Программа обрабатывает ошибку ValueError пока пользователь не введет число. Программа не крашится.
while True:
    try:
        enter = float(input("Введите число: "))
    except ValueError:
        print("ValueError. Вы ввели не число. Повторите ввод")

# Обработка исключений в бесконечном цикле.
# выход из цикла при успешном вводе, если пользователь вводит число
while True:
    try:
        enter = float(input("Введите число: "))
        print("Вы ввели число "+str(int(enter))+". Программа завершена")
        break
    except ValueError:
        print("ValueError. Вы ввели не число. Повторите ввод")

# Многократная обработка исключений в бесконечном цикле.
# обработка двух ошибок: введено не число, затем пользователь пытается делить на ноль
# ValueError и ZeroDivisionError: float division by zero
while True:
    try:
        enter = float(input("Введите число: "))
        print("Вы ввели число. Произвожу вычисление")
        result = 100/enter
        print("Рзультат", result)
    # при попытке ввести букву ValueError: could not convert string to float: 'h'
    except ValueError:
        print("ValueError. Вы ввели не число. Повторите ввод")
    # при попытке ввести число ноль ZeroDivisionError: float division by zero    
    except ZeroDivisionError:
         print("ZeroDivisionError. Деление на ноль. Повторите ввод")

# Необязательный оператор 'else'. Его код исполнится, если не было ошибки в боле 'try'
# Итоговый вывод можно поместить в оператор 'else'
while True:
    try:
        enter = float(input("Введите число: "))
        print("Вы ввели число. Произвожу вычисление")
        result = 100/enter
    # при попытке ввести букву ValueError: could not convert string to float: 'h'
    except ValueError:
        print("ValueError. Вы ввели не число. Повторите ввод")
    # при попытке ввести число ноль ZeroDivisionError: float division by zero    
    except ZeroDivisionError:
         print("ZeroDivisionError. Деление на ноль. Повторите ввод")
    # итоговый вывод
    else:
        print("Рзультат", result)

# Оператор 'finally'. Блок кода, который прописан в 'finally' исполняется ВСЕГДА. Даже после обработки
# исключений. Добавим переменную-счеткик прохождения цикла 'count'.
count = 0
while True:
    try:
        enter = float(input("Введите число: "))
        print("Вы ввели число. Произвожу вычисление")
        result = 100/enter
    # при попытке ввести букву ValueError: could not convert string to float: 'h'
    except ValueError:
        print("ValueError. Вы ввели не число. Повторите ввод")
    # при попытке ввести число ноль ZeroDivisionError: float division by zero    
    except ZeroDivisionError:
         print("ZeroDivisionError. Деление на ноль. Повторите ввод")
    # итоговый вывод
    else:
        print("Рзультат", result)
    # выполняется ВСЕГДА
    finally:
        count += 1
        print("Цикл "+str(count)+" завершен")

#!!! Поскольку оператор 'finally' выполняется ВСЕГДА, в него можно передать следующее:

# - экстренное сохранение данных
# - корректное закрытие файла
# - закрытие защищенного соединения с базой данных
# - методы, позволяющие избежать потерю данных при обрушении программы3
# - и многое др.


# Парсинг данных на примере такстового документа.

# Создание первого файла Text1.txt
r = open("path_to_file\\Text1.txt",
        "w", encoding="utf-8") # записать "w", кодировка "utf-8"
r.write("Информация из первого") # запись информации
r.close() # закрыть файл

# Создание второго файла Text2.txt
r = open("path_to_file\\Text2.txt",
        "w", encoding="utf-8") # записать "w", кодировка "utf-8"
r.write("Информация из второго") # запись информации
r.close() # закрыть файл

# Создание третьего файла Text3.txt
r = open("path_to_file\\Text3.txt",
        "w", encoding="utf-8") # записать "w", кодировка "utf-8"
r.write("Информация из третьего") # запись информации
r.close() # закрыть файл

# Создание четвертого файла Text4.txt
r = open("path_to_file\\Text4.txt",
        "w", encoding="utf-8") # записать "w", кодировка "utf-8"
r.write("Информация из четвертого") # запись информации
r.close() # закрыть файл

import sys

# url_list = ["Text1.txt", "Text2.txt", "Text3.txt", "Text4.txt"]
# поскольку исполняемый файл test.py не находится в корневом каталоге с файлами, необходимо прописать
# адреса в списке url_list
# пример написания длинных строк
url_list = [("path_to_file\\Text1.txt"), ("path_to_file\\Text2.txt"), ("path_to_file"
    "\\Text33.txt"), ("path_to_file\\Text4.txt")]

list_defect = []

list_info = []

# Итерируем список url адресов
for i, url in enumerate(url_list):
    print(i, '-->', url)

# если какого-то файла, указанного в списке нет url_list не существует (он не создан в системе), возникает
# ошибка
# код ошибки, если файла "Text33.txt" не существует:
# FileNotFoundError: [Errno 2] No such file or directory: 'path_to_file\\Text33.txt'

# Чтобы избежать обвала программы, обработаем исключение FileNotFoundError в циле итераций
# url, которые удалось спарсить добавляем в спсок list_info, а дефектные в список list_defect
for url in url_list:
    try:
        r = open(i)
        print(r.read())
        list_info.append(r.read())
        print("OK")
    except FileNotFoundError:
        print("FileNotFoundError. Url не найден.")
        list_defect.append(url)
        print("NOK")
        continue

# Если происходит экстренное обрушение программы.
# смоделируем при помощи метода sys.exit()
for url in url_list:
    try:
        r = open(url, encoding="utf-8")
        print(r.read())
        list_info.append(r.read())
        print(list_info)
        print("OK")
    except FileNotFoundError:
        print("FileNotFoundError. Url не найден.")
        list_defect.append(url)
        print(list_defect)
        print("NOK")
        sys.exit()
        continue

# чтобы избежать потери информации после обвала программы, используем оператор finally
try:
    # итерируем список адресов url_list
    for url in url_list:
        # попытка обработать ошибку, если таковая возникнет
        try:
            # открываем url адрес
            r = open(url, encoding="utf-8")
            print("Адрес url найден")
            # добавляем содержимое файла в список list_info
            list_info.append(r.read())
        # обработка адресов, которые не получилось спарсить (или которых нет в системе)
        except Exception:
            # url с которых не получилось взять информацию добавляем в список list_defect
            list_defect.append(url)
            print("FileNotFoundError. Адрес url не найден")
            # имитация обрушения программы
            sys.exit()
            continue

finally:
    # открываем файл Save.txt на чтение и дозапись информации в конец файла. Создается, если его нет
    r = open("path_to_file\\Save.txt",
        "a", encoding="utf-8") # открыть для дозаписи в конец файла, кодировка "utf-8"
    # итерируем список list_info адресов
    for i in list_info:
        # записываем в файл Save.txt информацию из открывшихся до обвала программы url адресов
        r.write(i)
    # выводим на экран данные, сохраненные в list_defect
    print(list_defect)
    # выводим список с информацией из открывшихся до обвала программы url адресов
    print(list_info)
    # записываем в файл файл Save.txt данные из list_defect, переводя их в строку 
    r.write(str(list_defect))
    # закрываем файл Save.txt
    r.close()
    print("Краш программы. Данные сохранены в файле 'Save.txt'")
