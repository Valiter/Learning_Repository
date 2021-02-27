
"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import cycle


def a_iter():
    ls = []
    start = input("Start num (End num is 50): ")
    for el in count(int(start)):
        ls.append(el)
        if el > 49:
            return ls


def b_iter(lst):
    for el in cycle(lst):
        print(el)
        if el > 49:
            return True


lst = a_iter()
b_iter(lst)
