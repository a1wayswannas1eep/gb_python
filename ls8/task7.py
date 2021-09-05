# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма num1 и num2 равна:')
        return f'num = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение num1 и num2 равно:')
        return f'num = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'num = {self.a} + {self.b} * i'


num1 = Complex(4, 10)
num2 = Complex(6, -6)
print(num1)
print(num2)
print(num1 + num2)
print(num1 * num2)
