# Python_Hub_Studio
# Python_7_Hours

# ОБЛАСТИ ВИДИМОСТИ ПЕРЕМЕННЫХ. Зарезервированные слова 'global' и 'nonlocal'

# Значения переменных (например 'x') относятся к глобальной области видимости.
x = 5

# Циклы 'while' и 'for' относятся к глобальной области видимости.
count = 0
while count < 3:
	count += 1

print(count) # OUT: 3

# Значение переменной 'x' в глобальной области видимости, функция его видит.
x = 5
def some_function():
	print(x)

some_function() # OUT: 5

# Переменные, объявленные в функции (например 'y') существуют в локальной области видимости,
# передать их глобальную область видимости можно при помощи оператора 'return', и то
# при этом происходит передача НЕ ПЕРЕМЕННОЙ, а ЗНАЧЕНИЯ, которое в ней содержится.
x = 5
def some_function():
	y = 10
	print(x)

some_function() # OUT: 5
print(y) # OUT: NameError: name 'y' is not defined

# Возвращаем значение 'y', записываем его в переменную 'some_number'. Ошибки не происходит.
# Переменную 'y' по прежнему вызвать не получится.
def some_function():
	y = 10
	return y

some_number = some_function()
print(some_number) # OUT: 10

# Ситуация при которой переменная 'x' в глобальной области видимости (x = 5) и 
# переменная 'x' в локальной области видимости (x = 10).
# Переменная 'x' не меняет своего значения, если объявлена локально.
x = 5
def some_function():
	x = 10
	print(x)

some_function() # OUT: 10
print(x) # OUT: 5

# При помощи ключевого слова 'global' переменная 'x' обьявляется в функции глобально.
# Переменная 'x' при этом меняет свое значение.
x = 5
def some_function():
	# переменная 'x' обьявляется глобально и её значение меняется на x = 10
	global x
	x = 10
	print(x)

some_function() # OUT: 10
print(x) # OUT: 10

# Если переменная объявлена глобально, её значение можно использовать и другой функцией.
def some_function2():
	# переменная 'x' обьявляется глобально и её значение меняется на x = 10
	print(x)

some_function2() # OUT: 10

# Функция some_function() возвращает (return) значение x = 100, при этом это значение
# присваивается переменной 'some_number'. Переменная 'x' при этом не меняет своего значения.
x = 5
def some_function():
	x = 100
	return x

some_number = some_function()

def some_function2(): #parametr
	print(x)

some_function2() # OUT: 5

# В программах, которые содержат огромное количество строк кода объявление переменной 
# в функции 'global' не приветствуется, т.к. такое изменение переменной проблемматично
# отследить оперативно. Код должен иметь структурированный вид.
x = 5
def some_function():
	# функция выполняет результат срабатывания функции some_function2(),
	# которая принимает в качестве аргумента x = 100
	x = 100
	return some_function2(x)

def some_function2(par):
	# функция содержит параметр 'par' и выводит его на print()
	print(par)

some_function() # OUT: 100

# Функция объявлена в функции.
x = 5
def some_function():
	x = 10
	def some_function2():
		# функция some_function2() выводит на печать значение x = 100
		x = 100
		print(x)
	# функция some_function() вызывает срабатывание функции some_function2()
	some_function2()
	# функция some_function() выводит на печать значение x = 10
	print(x)

# OUT: 100
#      10
some_function()
print(x) # OUT: 5

# Зарезервированное слово 'nonlocal'. Используется ТОЛЬКО ВО ВЛОЖЕННЫХ ФУНКЦИЯХ.
x = 5
def some_function():
	x = 10
	def some_function2():
		# слово 'nonlocal' изменяет значение 'x' в материнской функции some_function() 
		# переменная 'x' НЕ СОЗДАЕТСЯ, значение 'x' МЕНЯЕТСЯ с 10 на 100
		# функция some_function2() выводит на печать значение x = 100
		nonlocal x
		x = 100
		print(x)
	# функция some_function() вызывает срабатывание функции some_function2()
	some_function2()
	# функция some_function() выводит на печать значение x = 10
	print(x)
# OUT: 100
#      100
some_function()
print(x) # OUT: 5
