"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    # Atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Forvard!")

    def stop(self):
        print("Back!!")

    def turn(self, direction):
        print(f"We are going {direction}!")

    def show_speed(self):
        pass


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Warning {self}! Your speed is to big!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Warning {self}! Your speed is to big!")

class PoliceCar(Car):
    pass


police_car = PoliceCar(60, "white", "PP", True)
work_car = WorkCar(45, "red", "ww", False)
sport_car = SportCar(240, "green", "spp", False)
town_car = TownCar(65, "black", "Tu154", False)
town_car.show_speed()
work_car.show_speed()

work_car.turn("right")
town_car.go()
town_car.stop()



# def asking_function():
#     speed = input("speed: ")
#     color = input("color: ")
#     name = input("name: ")
#     is_police = input("Police or not? (true/false) ")
#     return speed, color, name, is_police
#
# act = True
# while act == True:
#     choise = int(input("Choose a number: "))
#     if choise == 1:
#         a = asking_function
#         print(a)
#         town_car = TownCar(a)
#     elif choise == 2:
#         asking_function
#         sport_car = SportCar(speed, color, name, is_police)
#     elif choise == 2:
#         asking_function
#         work_car = WorkCar(speed, color, name, is_police)
#     elif choise == 2:
#         asking_function
#         police_car = PoliceCar(speed, color, name, is_police)
#     else:
#         print("Stopping programm.")
#         act = False
