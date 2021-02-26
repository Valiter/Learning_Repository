"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

"""Мы импортируем функцию из второго задания, чтобы не писать генератор с нуля."""

from lesson_4_task_2 import list_generator


def sort(list):
    st = set(list)
    list_res = []
    i = 0
    for el in list:
        try:
            if el in st:
                list_res.append(el)
                st.remove(el)
        except Exception as err:
            print(Exception, err)
    return list_res


# Оно работает, но я этим удивлен.
list_2 = list_generator(10, 20)
print(list_2)
print(sort(list_2))
t = type(sort(list_2))
print(t)