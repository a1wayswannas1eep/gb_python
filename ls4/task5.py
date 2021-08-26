# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

my_list = [num for num in range(100, 1000) if num % 2 == 0]


def my_func(r_num, num):
    return r_num * num


print(f'Результат: {reduce(my_func, my_list)}')
