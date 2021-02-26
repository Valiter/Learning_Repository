def my_fync_operand(x, y):
    result_1 = x ** y
    return result_1

def my_fync_cycle(x, y):
    y = y * -1
    tic = 1
    middle = x
    while tic < y:
        middle = middle * x
        tic += 1
    result_2 = 1 / middle
    return result_2

def logic():
    while True:
        x = int(input(""))
        y = int(input(""))
        if x > -1 and y < 0:
            print(f"Numbers are {x} and {y}")
            return x, y
            break
        else:
            print("Nope.\nTry again!\n")

while True:
    x, y = logic()
    print(my_fync_operand(x, y))
    print(my_fync_cycle(x, y))
    if input("Нажмите Q, чтобы выйти: ").upper() == "Q":
        break
