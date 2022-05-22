# Python_Hub_Studio
# Python_7_Hours

# ЦИКЛ for

# для вывода данных воспользуемся функцией
def choose_plural(amount: int, variants: iter):
    '''Функция выбора формы существительного'''
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
            (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return "{} {}".format(amount, variants[variant])


string = "this_string" # итерируемая строка
count = 0 # переменная-счетчик. Определяет сколько раз повторяется заданное событие.

for i in string:
	if i == "t":
		print("Обнаружена буква 't'.")
		count += 1
	elif i == "s":
		# событие, про котором пропускается print(i), то есть буква "s" не печатается.
		continue
	print(i)
# необязательный цикл 'else', которым можно подвести итог итераций строки. Относится к циклу for
# если в цикле for встречается оператор 'break', необяательный цикл 'else' не сработает.
else:
	print("Цикл завершен.")
	print("В строке буква 't' встречается " + str(choose_plural(count, ("раз.", "раза.", "раз."))))
