# Python_Hub_Studio
# Python ООП уроки для начинающих с нуля, курс python ООП за три урока.
# Урок_№3.Декораторы методов класса.

'''
Рассмотрим четыре декоратора методов класса:
1. @property - gettr/вычисляемое свойство
2. @method.setter - setter (связанный с getter)
3. @classmethod
4. @staticmethod
'''

# 1 Без декораторов.
# Создадим объект 'x' экземпляр класса Player (игрок). Далее при помощи метода изменим значение свойства
# 'lvl' объекта 'x'. Без использования декораторов используется два разных метода 'get_lvl' и 'set_lvl'.
from datetime import datetime


class Player():
    '''Класс Player. Создает игроков'''

    __LVL, __HEALTH = 1, 100
    __slots = ["__lvl", "__health", "__born"]

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()


    def get_lvl(self):
        '''Возвращает текущий лвл персонажа'''
        return self.__lvl


    def set_lvl(self, numeric):
        '''Увеличсивает текущий уровень персонажа на величину numeric'''
        self.__lvl += numeric


x = Player()
print(x.get_lvl()) # OUT: 1
x.set_lvl(2) # меняет значение, но ни чего не возвращает
print(x.get_lvl()) # OUT: 3

print() # пустая строка


# 2 Декораторы @property (getter) и @method.setter (setter).
# Создадим объект 'x' экземпляр класса Player (игрок). Далее при помощи метода изменим значение свойства
# 'lvl' объекта 'x'. Используются два метода 'lvl', к которым применены декораторы @property (getter) и
# @method.setter (setter).
from datetime import datetime


class Player():
    '''Класс Player. Создает игроков'''

    __LVL, __HEALTH = 1, 100
    __slots = ["__lvl", "__health", "__born"]

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()


    @property
    def lvl(self):
        '''Возвращает текущий уровень персонажа'''
        return self.__lvl


    @lvl.setter
    def lvl(self, numeric):
        '''Увеличсивает текущий уровень персонажа на величину numeric'''
        self.__lvl += numeric


x = Player()
print(x.lvl) # OUT: 1
x.lvl = 2 # так прописывается увеличение 'lvl' на 2
print(x.lvl) # OUT: 3

print() # пустая строка


# 3 Декораторы @property (getter), @method.setter (setter), @classmethod
# Перед созданием экземпляра класса прописан классовый метод. Этот метод позволяет указывать каого уровня
# или с каким количеством здоровья создавать игроков. Создадим объект 'x' экземпляр класса Player (игрок),
# уровень которого при создании будет равен 10. Создадим объект 'y' экземпляр класса Player (игрок),
# уровень которого при создании будет равен 1. Уровень здоровья у 'x' и у 'y' будет равен 100 единицам.
from datetime import datetime


class Player():
    '''Класс Player. Создает игроков'''

    __LVL, __HEALTH = 1, 100
    __slots = ["__lvl", "__health", "__born"]

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()


    @property
    def lvl(self):
        '''Возвращает кортеж из двух значений. Первое - текущий уровень персонажа.
        Второе - количество времени, которое персонаж существует'''
        return self.__lvl, f"{datetime.now() - self.__born}"


    @lvl.setter
    def lvl(self, numeric):
        '''Увеличсивает текущий уровень персонажа на величину numeric.
        Установлено ограничение, запрещающее повышать уровень больше 100'''
        self.__lvl += numeric
        if self.__lvl >= 100: self.__lvl = 100


    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = lvl
        cls.__HEALTH = health


Player.set_cls_field(10)
x = Player()
print(x.lvl) # OUT: (10, '0:00:00')

Player.set_cls_field()
y = Player()
print(y.lvl) # OUT: (1, '0:00:00')

print() # пустая строка


# 4 Декораторы @property (getter), @method.setter (setter), @classmethod, @staticmethod
# Перед созданием экземпляра класса прописан классовый метод. Этот метод позволяет указывать каого уровня
# или с каким количеством здоровья создавать игроков. Создадим объект 'x' экземпляр класса Player (игрок),
# уровень которого при создании будет равен 10. Создадим объект 'y' экземпляр класса Player (игрок),
# уровень которого при создании будет равен 1. Уровень здоровья у 'x' и у 'y' будет равен 100 единицам.
# При помощи статического метода __typeTest добавлена проверка на передаваемые значения в __health и
# __lvl на тип данных целое число. 
from datetime import datetime


class Player():
    '''Класс Player. Создает игроков'''

    __LVL, __HEALTH = 1, 100
    __slots = ["__lvl", "__health", "__born"]

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()


    @property
    def lvl(self):
        '''Возвращает кортеж из двух значений. Первое - текущий уровень персонажа.
        Второе - количество времени, которое персонаж существует'''
        return self.__lvl, f"{datetime.now() - self.__born}"


    @lvl.setter
    def lvl(self, numeric):
        '''Увеличсивает текущий уровень персонажа на величину numeric.
        Установлено ограничение, запрещающее повышать уровень больше 100'''
        self.__lvl += Player.__typeTest(numeric)
        if self.__lvl >= 100: self.__lvl = 100


    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)


    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError ("Must be integer")


Player.set_cls_field(10)
x = Player()
print(x.lvl) # OUT: (10, '0:00:00')

Player.set_cls_field()
y = Player()
print(y.lvl) # OUT: (1, '0:00:00')
# при попытке увеличить уровень персонажа на 2.3 единицы программа вылетает с TypeError
# y.lvl = 2.3 # OUT: TypeError: Must be integer
