sum_num = 0
work = True
while work == True:
    print("U can write every symbol after numbers to finish the programm.")
    numbers = input("Put a number: ")
    list_of_numbers = []
    for el in numbers.split():
        list_of_numbers.append(el)
    for el in list_of_numbers:
        try:
            sum_num = int(sum_num) + int(el)
        except:
            print(f"Symbol was found: {el}.")
            work = False
    print(list_of_numbers)
    print(sum_num)