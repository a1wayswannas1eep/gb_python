# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные
# и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class Error(Exception):

    def __init__(self, text: str):
        self.text = text


def main():
    my_list = []

    while True:
        user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")

        if "stop" == user_input:
            break

        try:
            my_list.append(int(user_input))
        except Error as i:
            print(i)

    print(my_list)


main()
