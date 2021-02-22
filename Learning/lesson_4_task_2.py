"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

from random import randrange

# Говнокод-1
def shit_code(list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]):
    n = 0
    res_list = []
    tr = True
    while tr == True:
        print(f"Берем индекс элемента списка - {n}.")
        try:
            first_el = list[n]
            n += 1
            second_el = list[n]
            print(f"Производим сравнение элементов {first_el} и {second_el}")
            if first_el < second_el:
                res_list.append(list[n])
        except:
            print(f"Список {list} закончился.")
            tr = False
    return (f"Итоговый список - {res_list}")

# Говнокод-2
def good_code(height, length):
    list = [randrange(int(height)) for _ in range(int(length))]
    print("Список сгенерирован.")
    return list

height = input("Введите численный потолок: ")
length = input("Введите длинну списка: ")
print(good_code(height, length))
print(shit_code(good_code(height, length)))
