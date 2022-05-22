# Python_Hub_Studio
# Python_7_Hours

# Модуль tkinter
# Игра: "Dice Game"

import winsound, random, time

from tkinter import *
from threading import Thread


def throw():
    '''Функция броска.
    Рандомно выбирает кость'''
    path = "D:\\Python\\Test\\Python_Lessons\\Python_Hub_Studio\\26.tkinter.Dice_Game\\png\\"
    x = random.choice([
        path+"b1.png",
        path+"b2.png",
        path+"b3.png",
        path+"b4.png",
        path+"b5.png",
        path+"b6.png"
        ])
    return x

def img(event):
    '''Функция запускает событие'''
    path = "D:\\Python\\Test\\Python_Lessons\\Python_Hub_Studio\\26.tkinter.Dice_Game\\wav\\"
    def music():winsound.PlaySound(path+"dice.wav", False)
    Thread(target = music, daemon=True).start()
    global b1, b2
    for i in range(20):
        b1 = PhotoImage(file=(throw()))
        b2 = PhotoImage(file=(throw()))
        lab1["image"] = b1
        lab2["image"] = b2
        root.update()
        time.sleep(0.12)


# определение главного окна
root = Tk()

# определение размеров окна
root.geometry("400x200")

# title (шапка) окна
root.title("Dice Game")

# фиксирование размера окна (запрещает растягивание окна)
root.resizable(height=False, width=False)

# добавление собственной картинки в title (шапку)
icon_path = "D:\\Python\\Test\\Python_Lessons\\Python_Hub_Studio\\26.tkinter.Dice_Game\\png\\"
root.iconphoto(True, PhotoImage(
    file=icon_path+"iconka.png"))

# присвоение данных переменной (путь к картинке холста). Это стандартный зелёный холст
canvas_path = "D:\\Python\\Test\\Python_Lessons\\Python_Hub_Studio\\26.tkinter.Dice_Game\\png\\"
font = PhotoImage(
    file=canvas_path+"canvas.png")

# размещение холста на окне root, передача текста (при необходимости), передача фона (картинки холста)
# Это стандартный зелёный холст
Label(root, image=font).pack()

# создание первого места для броска кубика (слева холста)
lab1 = Label(root)

# указать место, где разместить первый кубик. передать положение по оси x, положение по оси y и "якорь"
# (положение центр). Возможная градация relx от 0 до 1 и градация rely от 0 до 1.
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)

# создание второго места для броска кубика (справа холста)
lab2 = Label(root)

# указать место, где разместить второй кубик. передать положение по оси x, положение по оси y и "якорь"
# (положение центр). Возможная градация relx от 0 до 1 и градация rely от 0 до 1.
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

# кнопка
# обработчик событий передает по нажатию ЛКМ "<1>" функция img()
root.bind("<1>", img)

# запуск программы начинается с броска кубиков (убирает две пустые метки/якоря на старте)
img("event")

# замыкание цикла
root.mainloop()
