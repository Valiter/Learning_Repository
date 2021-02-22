"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
"""

from copy import deepcopy

a = 0
dct = {"название":"", "цена":"", "количество":"", "единица измерения":""}
lst = []
nltcs = {"название":[], "цена":[], "количество":[], "единица измерения":[]}

while True:
    for el in dct.keys():
        dct[el] = input(f"Введите значение для графы '{el}': ")
        nltcs[el].append(dct[el])
    a += 1
    lst.append((a, deepcopy(dct)))

    print("===" * 5, "\nСписок товаров:")
    for el in lst:
        print(el)
    print("===" * 5, "\nСводка по характеристикам:")
    print(nltcs)
    print("===" * 5, "\n")