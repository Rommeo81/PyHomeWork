"""
Реализовать базовый класс Worker (работник).
    ● определить атрибуты: name, surname, position (должность), income (доход);
    ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
        элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    ● создать класс Position (должность) на базе класса Worker;
    ● в классе Position реализовать методы получения полного имени сотрудника
        (get_full_name) и дохода с учётом премии (get_total_income);
    ● проверить работу примера на реальных данных: создать экземпляры класса Position,
        передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

# ====== решение задания 6.3 ============

class Worker:
    # создаем атрибуты класса, последний делаем защищенный со ссылкой на словарь
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

# создаем класс со ссылкой на атрибуты класса Worker
class Position(Worker):
    # создаем атрибуты со ссылкой на атрибуты в "родительском" классе Worker
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    # создаем команду получения полного имени и фамилии со ссылкой на класс Worker
    def get_full_name(self):
        return self.name + ' ' + self.surname + '. ' + self.position + '.'

    # создаем команду полного дохода с забором данных из словаря
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

# задаем данные для первого работника
Worker_1 = Position('Michael', 'Jordan', 'Basketball player', 25000, 2500)

# выводим данные первого работника с обработкой команд на экран
print(Worker_1.get_full_name())
print(Worker_1.get_total_income())
