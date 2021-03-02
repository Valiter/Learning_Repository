"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def counter_for_company(cm = "company_file.txt"):
    st = True
    money = []
    money_list = []
    file = open(cm)
    list = []
    length = 0
    n = 0
    try:
        while st == True:
            line = file.readline()
            ls = line.split(" - ")
            list.append(ls)
            length += 1
            if line == "":
                st = False
        file.close
        while n < length:
            print(list[n][1])
            money.append(list[n][1])
            n += 1

    except Exception as err:
        print(err)
    print(money)
    return money_list

res = counter_for_company()
print(res)


# incomes = []
# with open('task_3.txt', 'r') as f_o:
#     lines = f_o.readlines()
#
#     for line in lines:
#         name, income = line.split(",")
#         income = int(income)
#         incomes.append(income)
#         if income < 20000:
#             print(name)
#     print(sum(incomes) / len(incomes))
