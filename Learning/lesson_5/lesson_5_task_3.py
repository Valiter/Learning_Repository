
def counter_for_company(cm = "company_file.txt"):
    st = True
    file = open(cm)
    list = []
    while st == True:
        line = file.readline()
        ls = line.split(" - ")
        list.append(ls)
        if line == "":
            st = False
    file.close
    print(list)

counter_for_company()
