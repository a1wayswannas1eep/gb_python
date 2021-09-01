# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, mtrx):
        self.correct = True
        if mtrx:
            if isinstance(mtrx, list):
                self.row = 0
                self.col = 0
                for el in mtrx:
                    if isinstance(el, list):
                        if not self.row:
                            self.col = len(el)
                        if self.col and self.col == len(el):
                            self.row += 1

        if self.correct:
            self.matrix = mtrx

    def __str__(self):
        str_tmp = ""
        for el in self.matrix:
            str_tmp += "\n"
            for i in el:
                str_tmp += f"{str(i):<4} "
        return str_tmp

    def __add__(self, mtrx):
        tmp_row = []
        tmp_mtrx = []
        try:
            if self.col == mtrx.col and self.row == mtrx.row:
                for row_n in range(self.row):
                    for col_n in range(self.col):
                        tmp_row.append(self.matrix[row_n][col_n] + mtrx.matrix[row_n][col_n])
                    tmp_mtrx.append(tmp_row)
                    tmp_row = []

        except:
            print(f"Некорректная матрица: {mtrx}")
        return Matrix(tmp_mtrx)


a = Matrix([[1, 2],
            [3, 4],
            [5, 6]])
b = Matrix([[7, 8],
            [9, 10],
            [11, 12]])
c = Matrix([[2, 4, 6],
            [1, 3, 5],
            [7, 8, 9],
            [3, 2, 1]])

print(f"Создана матрица 'a' \n", a, "\n")
print(f"Создана матрица 'b' \n", b, "\n")
print(f"Создана матрица 'c' \n", c, "\n")
print(f"Сложение матриц 'a' и 'b'")
print(a, "\n   + ", b, f"\n\nРезультат сложения матриц 'a' и 'b' : \n{a + b}", "\n")
