# Вариант 1
def name_list(*args):
    print(first_name, second_name, city, mail, tel_number, sep=",", end=".")

first_name = input("First name: ")
second_name = input("Second name: ")
city = input("City: ")
mail = input("E-mail: ")
tel_number = input("Telephone number: ")
name_list(first_name, second_name, city, mail, tel_number)
print("\n")

# Вариант 2
def name_list_2(first_name_2, second_name_2, city_2, mail_2, tel_number_2):
    print(first_name_2, second_name_2, city_2, mail_2, tel_number_2, sep=",", end=".")

x = input("First name: ")
y = input("Second name: ")
z = input("City: ")
a = input("E-mail: ")
b = input("Telephone number: ")
name_list_2(first_name_2 = x, second_name_2 = y, city_2 = z, mail_2 = a, tel_number_2 = b)
