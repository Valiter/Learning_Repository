print('Калькулятор /(для/) чайников.')
turn = (input('Начать программу? (Да/Нет): '))

while turn == "Да":
    NumberOne = input('Введите первое число: ')
    NumberTwo = input('Введите второе число: ')
    task = input('Выберите математическое действие (+,-,*,/,%,**): ')
    if task == '+':
        print(float(NumberOne) + float(NumberTwo))
    elif task == "-":
        print(float(NumberOne) - float(NumberTwo))
    elif task == '*':
        print(float(NumberOne) * float(NumberTwo))
    elif task == '**':
        print(float(NumberOne) ** float(NumberTwo))
    elif task == '%':
        print(float(NumberOne) % float(NumberTwo))
    elif task == '/':
        print(float(NumberOne) / float(NumberTwo))
    else:
        print('Вы ничего не написали.')

    turn = "Да"
    turn = (input('Продолжить или нет? (Да/Нет): '))

    if turn == "Да":
        print("Продолжаем выполнение...")
    elif turn == "Нет":
        print("Завершаем программу...")
    else:
        print("Выбор не сделан.")
        print("Начинаем завершение программы...")


print('Программа закончена.')