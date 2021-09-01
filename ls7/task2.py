# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, i):
        self.name = "Одежда"
        self.parameter_name = "Параметр"
        if i and (isinstance(i, int) or isinstance(i, float)):
            self.parameter = i
        else:
            self.parameter = 0
            self.parameter_name = f"Ошибка параметра {str(i)}"
            print(self.parameter_name)

    def __str__(self):
        return f"{self.name} \n{self.parameter_name} - {self.parameter}"

    @abstractmethod
    def consumption(self):
        return self.parameter


class Coat(Clothing):
    def __init__(self, i):
        super().__init__(i)
        self.name = "Пальто"
        self.parameter_name = "Размер"

    @property
    def consumption(self):
        return self.parameter / 6.5 + 0.5


class Costume(Clothing):
    def __init__(self, i):
        super().__init__(i)
        self.name = "Костюм"
        self.parameter_name = "Рост"

    @property
    def consumption(self):
        return 2 * self.parameter + 0.3


my_coat = Coat(54)
print(my_coat)
my_costume = Costume(178)
print(my_costume)
print(f"Общий расход ткани: {my_coat.consumption + my_costume.consumption}")
