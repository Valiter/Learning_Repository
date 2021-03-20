"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, datestring):
        self.datestring = datestring

    @classmethod
    def number(cls, data: "Data"):
        return list(map(int, data.datestring.split("-")))

    @staticmethod
    def validation(data: "Data"):
        parsed_data = data.datestring.split("-")
        if len(parsed_data[2]) not in {2, 4}:
            raise ValueError("невалидный год")
        if not 1 <= int(parsed_data[0]) <= 12:
            raise ValueError("Невалидный месяц")
        if not 1 <= int(parsed_data[0]) <= 31:
            raise ValueError("Невалидное число")
        print("Валидация пройдета")

data = Data("10-01-2020")
data.validation(data)
print(f"Data.number(data)")
