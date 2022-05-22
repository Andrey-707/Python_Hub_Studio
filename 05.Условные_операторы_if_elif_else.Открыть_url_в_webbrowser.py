# Python_Hub_Studio
# Python_7_Hours

# УСЛОВНЫЕ ОПЕРАТОРЫ "if", "elif" и "else".

# Пример_1
# Результатом выполнения программы будет выполнение модулем os.system() команды "start https://youtube.com", что
# приведет к открытию выб-браузера и переходу по ссылке https://www.youtube.com/

import os # стандартный модуль Python, обеспечивает взаимодействие с операционной системой


url = input() # прописать: https://youtube.com

if 'https://' in url: # Срабатывает код в условии 'if'
    os.system('start ' + url)
    print("if")
elif 'www.' in url:
    site = 'https://' + url
    os.system('start ' + url)
    print("elif")
else:
    url = 'https://www.' + url
    os.system('start ' + url)
    print("else")


# Пример_2
# Результатом выполнения программы будет выполнение модулем os.system() команды "start https://www.youtube.com, что
# приведет к открытию выб-браузера и переходу по ссылке https://www.youtube.com/
import os # стандартный модуль Python, обеспечивает взаимодействие с операционной системой


url = input() # прописать: www.youtube.com

if 'https://' in url:
    os.system('start ' + url)
    print("if")
elif 'www.' in url: # Срабатывает код в условии 'elif'
    site = 'https://' + url
    os.system('start ' + url)
    print("elif")
else:
    url = 'https://www.' + url
    os.system('start ' + url)
    print("else")


# Пример_3
# Результатом выполнения программы будет выполнение модулем os.system() команды "start https://www.youtube.com, что
# приведет к открытию выб-браузера и переходу по ссылке https://www.youtube.com/
import os # стандартный модуль Python, обеспечивает взаимодействие с операционной системой


url = input() # прописать: youtube.com

if 'https://' in url:
    os.system('start ' + url)
    print("if")
elif 'www.' in url:
    site = 'https://' + url
    os.system('start ' + url)
    print("elif")
else: # Срабатывает код в условии 'else'
    url = 'https://www.' + url
    os.system('start ' + url)
    print("else")


# Пример_4
# Результатом выполнения программы будет выполнение модулем webbrowser.open() команды "https://www.youtube.com", что
# приведет к открытию выб-браузера, переходу по ссылке https://www.youtube.com/ и через 5 секунд будет
# запущена программа (например, winamp.exe)
import os # стандартный модуль Python, обеспечивает взаимодействие с операционной системой
import webbrowser

from time import sleep


url = 'www.youtube.com'
path = 'your_path_to_winamp'
progrem_name = 'winamp.exe'


if 'https://' in url:
    webbrowser.open(url)
    print("if")
elif 'www.' in url: # Срабатывает код в условии 'elif'
    site = 'https://' + url
    webbrowser.open(url)
    print("elif")
    sleep(5)
    os.startfile(path + '\\' + progrem_name)
else:
    url = 'https://www.' + url
    webbrowser.open(url)
    print("else")


# Пример_4
# Открывать 'url' в бесконечном цикле
import os
import sys
import time
import webbrowser


while True:
    url = input("Enter 'url' or 'exit': ")
    if 'https://' in url:
        webbrowser.open(url)
        print("Open Success", url)
    elif 'www.' in url:
        url = 'https://' + url
        webbrowser.open(url)
        print("Open Success", url)
    elif '.' in url:
        url = 'https://www.' + url
        webbrowser.open(url)
        print("Open Success", url)
    elif url == "exit":
        print("Close Browser")
        time.sleep(5)
        os.system('taskkill /F /IM chrome.exe') # закрыть браузер
        print("Close Program")
        time.sleep(3)
        sys.exit() # закрыть программу
    else:
        print("Open '{}' Failed".format(url)) # при вводе несуществующего 'url'