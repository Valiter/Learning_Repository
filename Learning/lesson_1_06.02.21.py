tz = ("Тех.Задание: ")
task1 = ("Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.")
task2 = ("Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.")
task3 = ("Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.")
task4 = ("Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.")
task5 = ("Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.")
task6 = ("Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.")
ProgActiv = input("Включить программу? ")
yes = {"Да", "да", "+", "Конечно", "конечно", "Запускай", "запускай", "Включай", "включай", "1", "Да, продолжай"}
no = {"Нет", "нет", "-", "0", "Отказываюсь", "отказываюсь", "не", "Не", "Не хочу", "не хочу", "Выключить", "выключить"}
while ProgActiv in yes:
    TaskNumber = int(input('Выберите номер задания от 1 до 6: '))
    # Код хреновый, надо бы упростить и убрать дублирование.
    # Глобально: Надо почистить написание строчек и проч.
    # Глобально: Надо посмотреть как вставлять в print разные типы данных.
    # Там как-то через %d или нечто пообное делалость.
    # Глобально: Как вариант: сделать "напоминалки" с описанием ТЗ.
    if TaskNumber == 1:
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
# Над переписать через %d/%f или через f строку. Но пока и так сойдет.
# И еще не ясно как получить (3719 сек) вывод в виде 01:01:59
# Вообще, если пользователь введет любой тип данных, то программа будет работать...
    elif TaskNumber == 2:
        print(tz)
        print(task2)
        sectime = int(input("Введите время в секундах: "))
        hour = 3600
        minute = 60
        st2_1 = sectime // hour
        st2_2 = sectime % hour
        int(st2_2)
        st2_3 = st2_2 // minute
        st2_4 = st2_2 % minute
        print(str(st2_1) + ":" + str(st2_3) + ":" + str(st2_4))
    elif TaskNumber == 3:
        print(tz)
        print(task3)
        # Итак. По-моему тут идет лишнее нагромождение из if/elif/else. Пока так.
        # Мы получаем то, что нужно.
        start_elif3 = input('Хотите проверить задание?: ')
        if start_elif3 in yes:
            n_number = input("Введите число и только число! ")
            n_number_2n = str(n_number) * 2
            n_number_3n = str(n_number) * 3
            print("Мы получили: " + n_number + " " + n_number_2n + " " + n_number_3n)
            print("Найдем сумму этих чисел!")
            n_number_sum = int(n_number) + int(n_number_2n) + int(n_number_3n)
            print(n_number_sum)
        elif start_elif3 == "Нет":
            print("Как хотите.")
        else:
            print('Вы не выбрали ни один из вариантов ответа.')
    elif TaskNumber == 4:
        print(tz)
        print(task4)
        print()
        print("Введите целое положительное число, чтобы мы смогли найти большее число в нем!")
        numfromuser = int(input("Число: "))
        needednum = 0
        while numfromuser > 0:
            nfulast = numfromuser % 10
            numfromuser = numfromuser // 10
            if needednum < nfulast:
                needednum = nfulast
        print('Самое большая цифра в вашем числе: ' + str(needednum))
    elif TaskNumber == 5:
        print(tz)
        print(task5)
        M_take = int(input("Введите выручку: "))
        M_give = int(input("Введите издержки: "))
        if M_take > M_give:
            print("Выручка больше издержек!")
            print("Давайте посчитаем рентабельность.")
            M_rent = M_take/M_give
            print("Соотношение следующее: " + str(M_rent))
            memofcomp = int(input("А сколько у вас сотрудников в компании? "))
            M_plus = M_take - M_give
            mem_plus = M_plus/memofcomp
            print("В вашей компании прибыль на одного сотрудника составляет " + str(mem_plus) + " У.Е.")
        elif M_take == M_give:
            print("Поразительно, но вы работаете в ноль.")
        elif M_take < M_give:
            print("Выручка меньше издержек.")
    elif TaskNumber == 6:
        print(tz)
        print(task6)
        # Итак, я не имею ни малейшего понятикя, каким образом ме убрать цифры помлпе тысячных/сотых.
        # Понимаю как отбросить дробь, но не убрать её часть.
        # Хотя помню как нам это объясняли на занятии. Надо бы проверить.
        runstart = int(input("Введите первичный результат: "))
        runnoless = int(input("Введите цель: "))
        runstart_rem = runstart
        day = 1
        while runstart < runnoless:
            runstart = runstart * 1.1
            print("День номер: " + str(day) + " " + str(runstart))
            day = day + 1
        print("Ответ: Спортсмен достиг своей цели на день номер " + str(day) + " .")
    else:
        print("Вы не выбрали номер ответа.")
    TaskNumber = 0
    ProgActiv = input('Продолжить выполнение программы? ')
print("Программа завершена.")