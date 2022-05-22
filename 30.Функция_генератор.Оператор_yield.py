# Python_Hub_Studio
# Python_7_Hours

# Функция генератор. Оператор yield
# оператор yield дает понять интерпретатору python, что фанкция является функцией генератором.

# создадим текстовый файл New_file1.txt
# по адресу D:\Python\Test\Python_Lessons\Python_Hub_Studio\30.Функция_генератор
# some_text = """строка текста
# с какой-то
# информацией"""

# with open("D:\\Python\\Test\\Python_Lessons\\Python_Hub_Studio\\30.Функция_генератор\\New_file1.txt",
#         "w", encoding="utf-8") as r: # открыть для записи 'w', кодировка "utf-8"
#     r.write(some_text)

def some():
    '''Функция считывает из файла информацию построчно.
    Возвращает данные в виде списка'''
    list_text = []
    with open("your_path\\New_file1.txt", encoding="utf-8") as r:
        for i in r:
            list_text.append(i)
        print(list_text)
        return list_text

for i in some():
    print(i.split())

# используем функцию генератор
# такой способ позволяет значительно сэкономить номщность компьютера, не загружая память
def some():
    '''Функция генератор считывает из файла информацию.
    НЕ СОЗДАЕТ список list_text.
    функция генератор выдает по одному значению за каждую итерацию цикла for'''
    with open("your_path\\New_file1.txt", encoding="utf-8") as r:
        for i in r:
            yield i

for i in some():
    print(i.split())

# результат выполнения функции можно записать в переменную и вызывать с помощью функции next()
p = some()
# print(next(p)) # выводит первую строку текста
# print(next(p)) # выводит вторую строку текста
# print(next(p)) # выводит третью строку текста

# то же самое можно запустить в цикле и выводить на печать
for i in p:
    print(i)
