"""
Реализовать класс Stationery (канцелярская принадлежность).
    ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    ● в каждом классе реализовать переопределение метода draw.
        Для каждого класса метод должен выводить уникальное сообщение;
    ● создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


# Создаем класс Stationery (канцелярская принадлежность)
class Stationary:
    # Определить в классе атрибут title (название)
    def __init__(self, title):
        self.title = title
    # Определяем в классе метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    def draw(self):
        return f'Запуск отрисовки {self.title}'

# Создаем дочерний класс Pen (ручка)
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    # В классе реализовываем переопределение метода draw.
    # Для каждого класса метод должен выводить уникальное сообщение;
    def draw(self):
        return f'Это {self.title}. Вы можете написать поэму!'

# Создаем дочерний класс Pencil (карандаш)
class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    # В классе реализовываем переопределение метода draw.
    # Для каждого класса метод должен выводить уникальное сообщение;
    def draw(self):
        return f'Это {self.title}. Вы можете нарисовать картину!'

# Создаем дочерний класс Handle (маркер)
class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    # В классе реализовываем переопределение метода draw.
    # Для каждого класса метод должен выводить уникальное сообщение;
    def draw(self):
        return f'Это {self.title}. Вы можете раскрасить раскраску!'

# Создать экземпляры классов
Stationary_1 = Pen('Ручка')
Stationary_2 = Pencil('Карандаш')
Stationary_3 = Handle('Маркер')

# Проверяем, что выведет описанный метод для каждого экземпляра.
print(Stationary_1.draw())
print(Stationary_2.draw())
print(Stationary_3.draw())
