ls = [1, "А", 1.3, False, 24]
print("Создать список и заполнить его элементами различных типов данных.\nРеализовать скрипт проверки типа данных каждого элемента.\nИспользовать функцию type() для проверки типа.\nЭлементы списка можно не запрашивать у пользователя, а указать явно, в программе.")
print("\n2 варианта в программе:\n1) Ввод пользователем вручную;\n2) Работа с уже заданным списком.")
type_of_prog = input("Введите вариант программы: ")
null = 0
if type_of_prog == "1":
    ls.clear()
    cycles = input("Сколько элементов вы ходите в списке?\nВведите значение: ")
    while null < int(cycles):
        el = input(f"Введите что-нибудь ({null+1}): ")
        ls.append(el)
        null += 1
    print(ls)
    null = 0
    ls_len = len(ls)
    while null < ls_len:
        print(type(ls[null]))
        null += 1
elif type_of_prog == "2":
    ls_len = len(ls)
    print(ls)
    while null < ls_len:
        print(type(ls[null]))
        null += 1
    null = 0
else:
    print("Вы не выбрали варианта ответа.")
    print("Будет запущена стандартная программа.")
    null = 0
print("Программа заваршена.")