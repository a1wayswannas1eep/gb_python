# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

range_len = random.randint(1, 10)

with open("test5.txt", "w") as my_file:
    for i in range(range_len - 1):
        my_file.write(str(random.randint(1, 10)))
        my_file.write(" ")
    my_file.write(str(random.randint(1, 10)))

with open("test5.txt", "r") as my_file:
    summa = my_file.readline()

summa = [int(x) for x in summa.split(" ")]
print('Сумма чисел равна: ', sum(summa))
