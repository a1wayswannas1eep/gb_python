# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

a = input("Введите ваше имя: ")
b = input("Введите вашу фамилию: ")
c = input("введите ваш год рождения: ")
d = input("Введите ваш город проживания: ")
e = input("Введите ваше емейл: ")
f = input("Введите ваш номер телефона: ")

def func(a, b, c, d, e, f):return list(func(a, b, c, d, e, f))

print(a, b, c, d, e, f)