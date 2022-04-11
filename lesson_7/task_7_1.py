"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


# ====== решение задания 7.1 ============

# создаем класс Matrix (матрица)
class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx

    # Реализовываем перегрузку метода __str__() для вывода матрицы в привычном виде
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.mtrx]))

    # Реализуем перегрузку метода __add__() для реализации операции
    # сложения двух объектов класса Matrix (двух матриц).
    def __add__(self, other):
        try:
            mtrx_sum = [[int(self.mtrx[i][j]) + int(other.mtrx[i][j]) for j in range(len(self.mtrx[i]))]
                         for i in range(len(self.mtrx))]
            return Matrix(mtrx_sum)
        # если размер ширины или длинны матрицы будут не совпадать, то выведем ошибку
        except IndexError:
            return f'Ошибка в размере матрицы!'

# задаем значения матриц
a = [[5, 18, 11], [6, 17, 23], [41, 50, 9]]
b = [[45, 8, 2], [6, 7, 93], [24, 5, 97]]

# выполняем действия в классе с каждой матрицей "а" и "b"
mtrx_1 = Matrix(a)
mtrx_2 = Matrix(b)
new_mtrx = mtrx_1 + mtrx_2

# выводим все на экран
print(f'Матрица 1:\n{Matrix(a)}\n')
print(f'Матрица 2:\n{Matrix.__str__(mtrx_2)}\n')

print(f'Результат сложения двух матриц:\n{(new_mtrx)}\n')


