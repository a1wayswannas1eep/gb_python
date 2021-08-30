# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# 5ое задание такое же, смысла делать его нет)

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} двигается'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'На данный момент скорость {self.name} : {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'На данный момент скорость {self.name} : {self.speed}')

        if self.speed > 60:
            return f'Скорость для {self.name} превышена!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'На данный момент скорость {self.name} : {self.speed}')

        if self.speed > 40:
            return f'Скорость для {self.name} превышена!Снизте скорость!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} машина полиции'
        else:
            return f'{self.name} машина не из полиции'


mclaren = SportCar(270, 'желтого', 'McLaren', False)
toyota = TownCar(59, 'белого', 'Toyota', False)
gazelle = WorkCar(75, 'бело-синего', 'GAZ', True)
vesta = PoliceCar(90, 'бело-синего', 'LADA', True)
print(gazelle.turn_left())
print(f'{gazelle.go()}  {gazelle.show_speed()}')
print(f'{gazelle.name}  {gazelle.color} цвета')
print(f'{gazelle.name}  полицейская? {gazelle.is_police}')
print(f'Если {toyota.turn_right()}, {mclaren.stop()}')
print(toyota.show_speed())
print(mclaren.show_speed())
print(f'{mclaren.name} полицейская? {mclaren.is_police}')
print(vesta.police())
print(vesta.show_speed())
