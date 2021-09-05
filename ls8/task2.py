# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):
    zerodev = "Делить на 0 нельзя!"

    def __str__(self):
        return self.zerodev


# noinspection PyTypeChecker
class Number(float):

    def __truediv__(self, other):
        if other is not None and not other:
            raise ZeroDivision

        return Number(float(self) / float(other))


def main():
    while True:

        try:
            dividend, divider = map(Number, input("Введите делимое и делитель через запятую: ").split(','))
            print(dividend / divider)

        except ZeroDivision as i:
            print(i)

        except ValueError as i:
            print(i)
            break


main()
