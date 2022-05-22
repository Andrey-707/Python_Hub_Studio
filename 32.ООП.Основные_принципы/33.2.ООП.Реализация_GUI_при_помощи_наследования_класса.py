# Python_Hub_Studio
# Python ООП уроки для начинающих с нуля, курс python ООП за три урока.
# Урок_№2.Наследование.

# Реализация GUI при помощи наследования класса
from tkinter import Tk, Button


# step_1
# Обычный способ вызова графического интерфейса
# root = Tk()
# root.mainloop()

# step_2
# Реализуем это при помощи наследования класса Tk
# class MyTk(Tk):
# 	def __init__(self):
# 		Tk.__init__(self)


# root = MyTk()
# root.mainloop()


# step_3
# далее создадим продвинутый GUI
class MyApp(Tk):

	def __init__(self):
		Tk.__init__(self)
		self.geometry("400x400") # разрешение окна
		self.set_UI()



	# Запуск класса Button внутри класса MyApp без наследования называется КОМПОЗИЦИЯ
	# Т.е. внутри объекта класса 'MyApp' создаются объекты друго класса - 'Button'
	def set_UI(self):
		Button(self, text="Press_ME").pack() # создание кнопки


root = MyApp()
root.mainloop()
