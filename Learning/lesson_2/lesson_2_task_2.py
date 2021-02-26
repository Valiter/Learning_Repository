l = [1, 2, 3, 4, 5, 6, 7]
l_len = len(l)
print(l)
last = l.pop(int(l_len) - 1)
l[0::2], l[1::2] = l[1::2], l[0::2]
l.append(last)
print(l)