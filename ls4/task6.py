# 6. Реализовать два небольших скрипта:
#
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# a)

from itertools import count

def my_count(start, stop):

    for num in count(start):
        if num > stop:
            break
        else:
            print(num)

my_count(start=int(input("Введите начало отсчета: ")), stop=int(input("Введите конец отчета: ")))

# б)

from itertools import cycle

def my_cycle(el, rep):
    num = 0
    r = cycle(el)
    while num < rep:
        print(next(r))
        num += 1

my_cycle(el = [1, 2, 3, 4, 5], rep = int(input("Введите число повторений элеметов: ")))


