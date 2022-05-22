# Python_Hub_Studio
# Python_7_Hours

# ФОРМАТИРОВАНИЕ СТРОК

enter = input("Your name: ")

s = "Hello"

# добавим значение из переменной enter в переменную s

# конкатенация строк
s = "Hello " + enter
print(s) # OUT: Hello Andrey

# добавим значение прямо в строку. Метод %s означает "поставить строку в неизменном виде"
s = "Hello %s" % enter
print(s) # OUT: Hello Andrey

# если необходимо в формат %s передать несколько значений, их нужно передать в виде кортежа (tuple)
s = "Hello %s, I'm Python%s" % enter, "Python"
print(s) # OUT: TypeError: not enough arguments for format string

# в даном случае ошибки не возникает
s = "Hello %s, I'm %s" % (enter, "Python")
print(s) # OUT: Hello Andrey, I'm Python


# МЕТОД СТРОКИ .format()

# стандартный метод
s = "Hello {}, I'm {}".format(enter, "Python")
print(s) # OUT: Hello Andrey, I'm Python

# нумерация передаваемых обьектов {0}, {1} и т.д.
s = "Hello {1}, I'm {0}".format(enter, "Python")
print(s) # OUT: Hello Python, I'm Andrey


# f-строка
who = "Python"
s = f"Hello {enter}, I'm {who}"
print(s) # OUT: Hello Andrey, I'm Python

# нельзя передавать строку в методе f-строка
s = f"Hello {enter}, I'm {"Python"}"
print(s) # OUT: SyntaxError: invalid syntax

# можно передавать арифметическое выражение в методе f-строка. Передача арифметического выражения {1+3*2}
s = f"Hello {enter}, I can do it {1+3*2}"
print(s) # OUT: Hello Andrey, I can do it 7

# можно передавать функции выражение в методе f-строка. Передача функции {len(who)}
who = "Python"
s = f"Hello {enter}, I'm {len(who)}"
print(s) # OUT: Hello Andrey, I'm 6
