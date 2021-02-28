
def counter_for_company(cm = "company_file.txt"):
    st = True
    money = 0
    money_list = []
    file = open(cm)
    list = []
    length = 0
    n = 0
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
        n += 1
    return money_list

res = counter_for_company()
print(res)
