"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

"""
Пометка: Не очень понял задание, когда скопипастил код - разобрался. Вывод - нужно подучить скрытые методы.
"""


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return Matrix(c)
        # return "\n".join(map(str, c))


a = [[1, 2, 3, 4],
     [1, 2, 3, 4],
     [1, 2, 3, 4]]
b = [[1, 2, 3, 4],
     [1, 2, 3, 4],
     [1, 2, 3, 4]]

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
