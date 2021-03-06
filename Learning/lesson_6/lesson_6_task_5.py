"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки”.
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Pen(Stationery):
    def __init__(self, title="ручка"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки ручки.")


class Pencil(Stationery):
    def __init__(self, title="карандаш"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки карандаша.")


class Handle(Stationery):
    def __init__(self, title="маркер"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки маркера.")


name = input("Введите название канцеляского товара: ")

state = Stationery(name)
pen = Pen()
pencil = Pencil()
handle = Handle()

state.draw()
pen.draw()
pencil.draw()
handle.draw()

print(pen.title)
print(pencil.title)
print(handle.title)
