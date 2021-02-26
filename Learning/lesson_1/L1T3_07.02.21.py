# Третье задание.
# Отрабатываем чертовы %d, %s и прочее.
n_number = input("Введите число и только число! ")
n_number_2n = str(n_number) * 2
n_number_3n = str(n_number) * 3
print("Мы получили: " "%s" % n_number, "%s" % n_number_2n, "%s" %  n_number_3n, sep=(" "))
print("Найдем сумму этих чисел!")
n_number_sum = int(n_number) + int(n_number_2n) + int(n_number_3n)
print(n_number_sum)