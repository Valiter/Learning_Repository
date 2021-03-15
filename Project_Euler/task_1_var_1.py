"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""


def sum_del_en_3_5(low_num=0, hight_num=1000):
    ls = []
    sum_num = 0
    for el in range(low_num, hight_num):
        if el % 3 == 0 or el % 5 == 0:
            ls.append(el)
            sum_num = sum_num + el
    return f"Start number is {low_num};\nEnd number is {hight_num}\nSum of all numbers is {sum_num}."


print(sum_del_en_3_5())
