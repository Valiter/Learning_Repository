string = input("Введите несколько слов через пробел: ")
list = string.split()
l_len = len(list)
null = 0
while null < l_len:
    print(f"{null + 1} {list[null][0:9:]}")
    null += 1