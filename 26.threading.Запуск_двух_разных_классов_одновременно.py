# Запуск двух разных классов одновременно. Потоковая обработка.

import winsound

from threading import Thread


# 1
def play_sound():
    # filename == путь к файлу
    # winsound.FILENAME можно установить значение False
    winsound.PlaySound(filename, winsound.FILENAME)

thread = Thread(target=play_sound)
thread.start()
print ('a')


# 2
# Более короткий способ запуска.
def music():winsound.PlaySound('dice.wav', False)
Thread(target=music, daemon=True).start()
print('b')