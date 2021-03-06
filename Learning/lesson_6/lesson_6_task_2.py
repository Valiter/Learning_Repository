"""
Реализовать класс Road (дорога),
в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.

Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    # Атрибуты
    def __init__(self, lenght, width):
        self._lenght_inside = lenght
        self._width_inside = width

    def formula(self):
        asphalt = self._lenght_inside * self._width_inside * 25 * 5
        print(asphalt)

a = input("Put a numbers of leght: ")
b = input("Put a numbers of width: ")
n_132 = Road(int(a), int(b))
n_132.formula()
