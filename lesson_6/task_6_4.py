"""
Реализуйте базовый класс Car.
    ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
        А также методы: go, stop, turn(direction), которые должны сообщать, что машина
        поехала, остановилась, повернула (куда);
    ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    ● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    ● для классов TownCar и WorkCar переопределите метод show_speed.
        При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат
"""

# ====== решение задания 6.4 ============

class Car:
    # создаем класс и атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # создаем методы
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    # добавлением в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля
    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'

#  создаем дочерний класс TownCar с унаследованием атрибутов из класса Car
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    #  добавлением метод show_speed по максимальной скорости для класса TownCar с обработкой на превышение
    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

#  Создаем дочерний класс SportCar с унаследованием атрибутов из класса Car.
#  В условии не сказана максимальная скорость для этого класса и что с ней делать. Будет ездить без штрафов =)
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

#  Создаем дочерний класс WorkCar с унаследованием атрибутов из класса Car
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    #  Добавлением метод show_speed по максимальной скорости для класса WorkCar с обработкой на превышение
    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car!'


#  Создаем дочерний класс PoliceCar с унаследованием атрибутов из класса Car
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    #  Добавлением метод police по проверке на полицию для класса PoliceCar с обработкой на превышение
    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

# Задаем параметры автомобилей (speed, color, name, is_police (булево))
car1 = SportCar(100, 'Red', 'Mustang', False)
car2 = TownCar(30, 'Yellow', 'Chrysler', False)
car3 = WorkCar(70, 'Black', 'Dodge', False)
car4 = PoliceCar(110, 'Blue', 'Ford', True)

# вызываем методы из классов и выводим результаты
print(car1.turn_left())

print(f'When {car2.turn_right()}, then {car3.stop()}')

print(f'{car1.go()} with speed exactly {car1.show_speed()}')

print(f'{car3.name} is {car3.color}')

print(f'{car1.name} a police car? {car1.is_police}')
print(f'{car4.name} a police car? {car4.is_police}')

print(car1.show_speed())
print(car2.show_speed())
print(car4.police())
print(car4.show_speed())
