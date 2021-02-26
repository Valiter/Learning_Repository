def sum_2_arg(a, b, c):
    max_1 = max(a, b)
    max_2 = max(b, c)
    max_3 = max(a, c)
    ls = [max_1, max_2, max_3]
    r_1 = max(ls)
    r_2 = min(ls)
    # Почему вариант кода
    # r_3 = sum(r_1, r_2)
    # Не работает?
    r_3 = r_1 + r_2
    return r_3

a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))
print(sum_2_arg(a, b, c))
