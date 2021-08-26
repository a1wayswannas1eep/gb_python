# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.

from math import factorial

def fact(n):

    for num in range(1, n + 1):
        yield factorial(num)

def main():
    n = input("Введите число операций: ")
    try:
        n = int(n)
    except ValueError:
        print("Ошибка!")

    for el in fact(n):
        print(el)

if __name__ == "__main__":
    main()


