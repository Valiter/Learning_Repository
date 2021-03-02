""" Не очень понятно как убрать подсчет пустых строчек, которые не несут никакой полезной информации."""


def count_str_words(name = "test_file.txt"):
    obj = open(name)
    str_num = 0
    wrd_num = 0
    for line in obj:
        print(line)
        str_num += 1
        for el in line.split(" "):
            wrd_num += 1
    obj.close()
    return str_num, wrd_num


count_str_words()
print(count_str_words())
