# Python_Hub_Studio
# Python ООП уроки для начинающих с нуля, курс python ООП за три урока.
# Урок_№2.Наследование.

# Импортируемый модуль class3. Используется в файле 33.ООП.Основные_принципы.Наследование.py

# Класса который не наследуется называется "super class"

class Verification():
	'''Класс Verification (проверка). Создает экземпляр класса, принимает из параметров
	(в __init__) 'login' и 'password', так же используется приватный метод __lenPassword(),
	который проверяет на надежность  'password' (при уловии len(self.password) < 8, то
	'password' не принимается) '''
	def __init__(self, login, password):
		self.login = login
		self.password = password
		self.__lenPassword()

	
	def __lenPassword(self): # 
		'''Проверка пароля по длине. К методу применена инкапсуляция.
		Метод используется только в классе'''
		if len(self.password) < 8:
			raise ValueError("Слабый пароль")


	def save(self):
		'''Сохранение данных. Открывает файл в режиме дозаписи ("a"), добавляет
		информацию в виде кортежа ('пользователь', 'пароль')'''
		with open("path_to_file\\Users.txt", "a") as a:
			a.write(f"{self.login, self.password}" + "\n")
