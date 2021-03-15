"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

from time import time


def sum_del_en_3_5(low_num=0, hight_num=1000):
    start = time()
    ls = []
    sum_num = 0
    for el in range(low_num, hight_num):
        if el % 3 == 0 or el % 5 == 0:
            sum_num = sum_num + el
    end = time()
    tm = str(end - start)[:7:]
    print(f"\nWorking time is {tm}")
    return f"Start number is {low_num};\nEnd number is {hight_num}\nSum of all numbers is {sum_num}."

low_num = input("Start number: ")
hight_num = input("End number: ")
print(sum_del_en_3_5(hight_num=int(hight_num), low_num=int(low_num)))
