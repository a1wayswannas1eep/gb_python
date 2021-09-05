# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        self.lists.update({equipment.serial_number: str([equipment.title, self])})
        print('На ' + str(self.title) + ' получено оборудование: '
              + str(equipment.title) + ' ,серийный номер: ' + str(equipment.serial_number))

    def give_to_depot(self, equipment, other):
        self.give_lists.update({equipment.serial_number: str([equipment.title, other])})
        print('Передано оборудование :' + str(equipment.title) + ' ,серийный номер: ' + str(
            equipment.serial_number))
        other.take_to_depot(equipment)

    def list_equipments(self):
        print('На ' + str(self.title) + ' получено оборудование: ')
        print(str(self.lists))
        print('Общее количество: ', len(self.lists))
        print('Со склада ' + str(self.title) + ' выдано оборудование: ')
        print(str(self.give_lists))
        print('Общее количество: ', len(self.give_lists))


class Office_equipment:
    def __init__(self, title: str, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)


class Printer(Office_equipment):
    def __init__(self, title, serial_number, print_velocity):
        Office_equipment.__init__(self, title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return 'Название модели: ' + Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title, serial_number, resolution):
        Office_equipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return 'Название модели: ' + Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.resolution)


class Copier(Office_equipment):
    def __init__(self, title, serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return 'Название модели: ' + Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.addit)


store1 = Depot('главный склад')
store2 = Depot('филиал')
a = Printer('HP', 223533, 1)
b = Scanner('Epson', 463534, 2)
c = Copier('Epson', 244552, 3)
d = Printer('HP', 765454, 4)
print(a)
print(b)
print(c)
store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)
store1.take_to_depot(d)
store1.give_to_depot(a, store2)
store1.list_equipments()
store2.list_equipments()
