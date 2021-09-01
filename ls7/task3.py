# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()),
# вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, x):
        if x and isinstance(x, int):
            self.count = x

    def __add__(self, cell):
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count + cell.count))

    def __sub__(self, cell):
        if cell and isinstance(cell, Cell):
            if (int(self.count - cell.count)) > 0:
                return Cell(int(self.count - cell.count))
            else:
                print("Ошибка!")

    def __mul__(self, cell):
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count * cell.count))

    def __truediv__(self, cell):
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count // cell.count))

    def __str__(self):
        return f"Клетка из {self.count} ячеек"

    def make_order(self, col):
        tmp_str = ""
        if col and isinstance(col, int):
            row = self.count // col
            row_end = self.count % col
            while row:
                tmp_str += ("*" * col) + "\n"
                row -= 1
            tmp_str += ("*" * row_end)
        return tmp_str


cell_1 = Cell(20)
cell_2 = Cell(10)
cell_3 = Cell(15)
cell_4 = Cell(68)
cell_5 = Cell(34)

print(f"Сложение: {cell_1 + cell_2}")
print(f"Вычитание: {cell_3 - cell_4}")
print(f"Вычитание№2: {cell_4 - cell_5}")
print(f"Умножение: {cell_2 * cell_3}")
print(f"Деление: {cell_4 / cell_1}")

print(f"Умножение (make_order):\n{(cell_2 * cell_3).make_order(12)}")
print(f"Деление (make_order):\n{(cell_4 / cell_1).make_order(5)}")
print(f"Клетка №5 (make_order:\n{cell_5.make_order(15)}")
