def file_rewriter(name = "name.txt"):
    f_obj = open(f"{name}", "a")
    start = 1
    while start == 1:
        string = input("W: ")
        f_obj.write(f"{string}\n")
        if string == "":
            start = 0
    f_obj.close()


file_rewriter()
