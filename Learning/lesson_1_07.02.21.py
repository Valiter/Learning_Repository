tz = ("Тех.Задание: ")
task1 = ("Поработайте с переменными, создайте несколько, выведите на экран,\n запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.")
task2 = ("Пользователь вводит время в секундах.\n Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.\n Используйте форматирование строк.")
task3 = ("Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.\n Например, пользователь ввёл число 3.\n Считаем 3 + 33 + 333 = 369.")
task4 = ("Пользователь вводит целое положительное число.\n Найдите самую большую цифру в числе.\n Для решения используйте цикл while и арифметические операции.")
task5 = ("Запросите у пользователя значения выручки и издержек фирмы.\n Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).\n Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).\n Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.")
task6 = ("Спортсмен занимается ежедневными пробежками.\n В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.\n Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.\n Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.")
Prog_Activ = input("Включить программу? ")
yes = {"Да", "да", "+", "Конечно", "конечно", "Запускай", "запускай", "Включай", "включай", "1", "Да, продолжай"}
no = {"Нет", "нет", "-", "0", "Отказываюсь", "отказываюсь", "не", "Не", "Не хочу", "не хочу", "Выключить", "выключить"}
while Prog_Activ in yes:
    Task_Number = int(input('Выберите номер задания от 1 до 6: '))
    if Task_Number == 1:
        print(tz)
        print(task1)
        per_str = "lalala"
        per_int = 123
        per_float = 1.2323
        per_bool = True
        tt = 0
        while tt < 2:
            tt = tt + 1
            print(per_str)
            print(per_int)
            print(per_float)
            print(per_bool)
            if tt == 1:
                per_str = input('Введите любые символы в строчку: ')
                per_int = int(input('Введите целое число: '))
                per_float = float(input('Введите число с плавающей точкой: '))
                per_bool = bool(input('Введите (True / False): '))
    elif Task_Number == 2:
        print(tz)
        print(task2)
        sectime = int(input("Введите время в секундах: "))
        hour_in_sec = 3600
        minute_in_sec = 60
        hour = sectime // hour_in_sec
        sec_after_hour = sectime % hour_in_sec
        minute = sec_after_hour // minute_in_sec
        seconds = sec_after_hour % minute_in_sec
        print("%02d" % hour, "%02d" % minute, "%02d" % seconds, sep=":")
    elif Task_Number == 3:
        print(tz)
        print(task3)
        n_number = input("Введите число и только число! ")
        n_number_2n = str(n_number) * 2
        n_number_3n = str(n_number) * 3
        print("Мы получили: " "%s" % n_number, "%s" % n_number_2n, "%s" % n_number_3n, sep=(" "))
        print("Найдем сумму этих чисел!")
        n_number_sum = int(n_number) + int(n_number_2n) + int(n_number_3n)
        print(n_number_sum)
    elif Task_Number == 4:
        print(tz)
        print(task4)
        print()
        print("Введите целое положительное число, чтобы мы смогли найти большее число в нем!")
        num_from_user = int(input("Число: "))
        needed_num = 0
        while num_from_user > 0:
            nfulast = num_from_user % 10
            num_from_user = num_from_user // 10
            if needed_num < nfulast:
                needed_num = nfulast
        print('Самое большая цифра в вашем числе: ' + str(needed_num))
    elif Task_Number == 5:
        print(tz)
        print(task5)
        M_take = int(input("Введите выручку: "))
        M_give = int(input("Введите издержки: "))
        if M_take > M_give:
            print("Выручка больше издержек!")
            print("Давайте посчитаем рентабельность.")
            M_rent = M_take/M_give
            print("Соотношение следующее: " + str(M_rent))
            mem_of_comp = int(input("А сколько у вас сотрудников в компании? "))
            M_plus = M_take - M_give
            mem_plus = M_plus/mem_of_comp
            mem_plus = round(mem_plus, 3)
            print(f"В вашей компании прибыль на одного сотрудника составляет {mem_plus} У.Е.")
        elif M_take == M_give:
            print("Поразительно, но вы работаете в ноль.")
        elif M_take < M_give:
            print("Выручка меньше издержек.")
    elif Task_Number == 6:
        print(tz)
        print(task6)
        run_start = int(input("Введите первичный результат: "))
        run_noless = int(input("Введите цель: "))
        run_start_rem = run_start
        day = 1
        while run_start < run_noless:
            run_start = run_start * 1.1
            run_start_v2 = round(run_start, 2)
            # Я нашел команду round!!! Ухуууууу! Я умею гуглить! Ахахаха.
            str_for_6 = "День номер {}, Спортсмен пробежал {} км.".format(day, run_start_v2)
            print(str_for_6)
            day = day + 1
        print("Ответ: Спортсмен достиг своей цели на", "%s" % day, "день.")
    else:
        print("Вы не выбрали номер ответа.")
    Task_Number = 0
    Prog_Activ = input('Продолжить выполнение программы? ')
print("Программа завершена.")
