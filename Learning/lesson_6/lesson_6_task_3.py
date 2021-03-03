"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    # Atributes
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Posision(Worker):
    def get_full_name(self):
        return (f"{self.name} {self.surname}")

    def get_total_inncome(self):
        sum_1 = self._income.get("wage")
        sum_2 = self._income.get("bonus")
        sum_3 = int(sum_1) + int(sum_2)
        print(sum_3)
        return sum_3

name = input(f"Name: ")
surname = input(f"Surname: ")
position = input(f"Position: ")
wage = input(f"Wage: ")
bonus = input(f"Bonus: ")
exp = Posision(name, surname, position, wage, bonus)
print(exp.get_full_name())
exp.get_total_inncome()
