"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


def money_to_pay(*args):
    result = (work * time) + prime
    return result


work_time = float(input("Количество проработанных часов: "))
money_per_hour = float(input("Ставка в час: "))
prime = float(input("Премия: "))
money_to_pay(work_time, money_per_hour, prime)