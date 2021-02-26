# Не работает очистка списка. Не понимаю почему.
# Не получилось реализовать выход из программы +дебаггер ругается на такой вариант программы.
# Не понимаю ошибки.

ls = []
stop = ("нет")
i = 0
answ_list = ["почистить", "да", "конечно", "1", "true"]

def int_func(strng):
    for el in strng.split():
        try:
            if int(el) == 0:
                global stop
                stop = 0
                break

        except:
            ls.append(el.title())

while stop == ("нет"):
    strng = input("Введите слово или слова: \n")
    print("HINT!\n0 в списке слов заканчивает выполнение программы.")
    int_func(strng)
    print(ls)
    i += 1
    if i == 2:
        print("Почистить список?")
        answer = input("Ответ: ").lower()
        if answer in answ_list:
            ls.clear()
            i = 0
        stop = input("Закончить программу?\n").lower