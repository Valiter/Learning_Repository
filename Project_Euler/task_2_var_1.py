"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""


def fibonachy(stop=4_000_000):
    num_first = 1
    num_second = 2
    num_third = 0
    num = 0
    while num_third < stop:
        num_third = num_first + num_second
        print(num_first, num_second)
        print(f"S:{num_third}")
        num_first = num_second
        num_second = num_third
        if num_third % 2 == 0:
            print(f"Amount: {num}")
            num += num_third
    return num


print(fibonachy())
