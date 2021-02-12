# Доделать.
list = [10, 7, 6, 4, 2]
number = int(input("Введите целое число: "))
try:
    print(list.index(number))
except:
    print("Числа нет в списке.")
finally:
    l_len = len(list)
    search_index = l_len / 2
    if list[search_index] < number:
    print(list.insert(search_index, number))
    print(list)
