# Python_Hub_Studio
# Python_7_Hours

# СЛОВАРИ.
# !!! СЛОВАРЬ ОТНОСИТСЯ К ИЗМЕНЯЕМЫМ ТИПАМ ДАННЫХ !!!

# ИТЕРАЦИЯ СЛОВАРЯ ПО КЛЮЧАМ.

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

# Добавить скидку 15% на товары из каталога.
for i in price:
	price[i] *= 0.85

print(price) # OUT: {'meat': 2.55, 'bread': 0.85, 'potato': 0.425, 'water': 0.17}

# После добавления скидки цена товара 'potato': 0.425 имеет ТРИ знака после запятой.

# Проитерируем значения словаря по ключам и применим округление значений до двух
# знаков после запятой.
for i in price:
	price[i] = round(price[i], 2)

print(price) # OUT: {'meat': 2.55, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}

# Оставить каталог без изменений и на его основе создать новый, цены на товар 
# которого имеют скидку 15%.
price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

new_price = {}
for i in price:
	new_price[i] = round(price[i]*0.85, 2)

print(price) # OUT: {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
print(new_price) # OUT: {'meat': 2.55, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}

# МЕТОД .items()

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

x = price.items()
print(x) # OUT: dict_items([('meat', 3), ('bread', 1), ('potato', 0.5), ('water', 0.2)]) 

# Метод .items() создает неполноценный список dict_items. Он создает объект-представление.
# Цель данного метода дальнейшая итерация списка-отображения.
print(type(x)) # OUT: <class 'dict_items'>

# При необходимости можно применить функцию .list() для преобразования списка-отображения
# dict_items в полноценный список.
print(list(x)) # OUT: [('meat', 3), ('bread', 1), ('potato', 0.5), ('water', 0.2)]

# ИТЕРАЦИЯ ПО ЭЛЕМЕНТАМ КЛЮЧ-ЗНАЧЕНИЕ с помощью метода .items()

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

for i in price.items():
	# OUT: ('meat', 3)
	# 	   ('bread', 1)
	#      ('potato', 0.5)
	# 	   ('water', 0.2)
	print(i)

# Данная итерация выдает кортежи, которые являются НЕИЗМЕНЯЕМЫМ ТИПОМ ДАННЫХ.
# Распакуем кортежи. Вместо 'key', 'value' могут быть ЛЮБЫЕ обозначения (переменные).
price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

for key, value in price.items():
	# OUT: meat 3
	# 	   bread 1
	# 	   potato 0.5
	# 	   water 0.2
	print(key, value)

# Можно применить текст для наглядности отображения.
for key, value in price.items():
	# OUT: Цена товара meat составляет 3 USD
	# 	   Цена товара bread составляет 1 USD
	# 	   Цена товара potato составляет 0.5 USD
	# 	   Цена товара water составляет 0.2 USD
	print("Цена товара", key, "составляет", value, "USD")

# ИНВЕРСИЯ элементов словаря ключ-значение. Или 'swap' элементов key-value

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}
new_price = {}

for key, value in price.items():
	new_price[value] = key

print(new_price) # OUT: {3: 'meat', 1: 'bread', 0.5: 'potato', 0.2: 'water'}

# МЕТОД .values()

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

x = price.values()
print(x) # OUT: dict_values([3, 1, 0.5, 0.2])

# Метод .values() создает неполноценный список dict_values. Он создает объект-представление.
# Цель данного метода дальнейшая итерация списка-отображения.
print(type(x)) # OUT: <class 'dict_values'>

# При необходимости можно применить функцию .list() для преобразования списка-отображения
# dict_values в полноценный список.
print(list(x)) # OUT: [3, 1, 0.5, 0.2]

# ИТЕРАЦИЯ ПО ЭЛЕМЕНТАМ КЛЮЧ-ЗНАЧЕНИЕ с помощью метода .values()

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

for i in price.values():
	# OUT: 3
	# 	   1
	# 	   0.5
	# 	   0.2
	print(i)

# МЕТОД .keys()

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

x = price.keys()
print(x) # OUT: dict_keys(['meat', 'bread', 'potato', 'water'])

# Метод .keys() создает неполноценный список dict_keys. Он создает объект-представление.
# Цель данного метода дальнейшая итерация списка-отображения.
print(type(x)) # OUT: <class 'dict_keys'>

# При необходимости можно применить функцию .list() для преобразования списка-отображения
# dict_keys в полноценный список.
print(list(x)) # OUT: ['meat', 'bread', 'potato', 'water']

# ИТЕРАЦИЯ ПО ЭЛЕМЕНТАМ КЛЮЧ-ЗНАЧЕНИЕ с помощью метода .keys()

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

for i in price.keys():
	# OUT: meat
	# 	   bread
	# 	   potato
	# 	   water
	print(i)

# Метод .keys() позволяет ЭКОНОМИТЬ вычислительную мощность.

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

# Добавить скидку 15% на товары из каталога. Итерация словаря по ключам.
# Оставить каталог без изменений и на его основе создать новый, цены на товар 
# которого имеют скидку 15%.

new_price = {}
for i in price.keys():
	new_price[i] = round(price[i]*0.85, 2)

print(price) # OUT: {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
print(new_price) # OUT: {'meat': 2.55, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}
