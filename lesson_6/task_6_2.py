"""
Реализовать класс Road (дорога).
    ● определить атрибуты: length (длина), width (ширина);
    ● значения атрибутов должны передаваться при создании экземпляра класса;
    ● атрибуты сделать защищёнными;
    ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
      толщиной в 1 см*число см толщины полотна;
    ● проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

# ====== решение задания 6.2 ============

# формируем класс с защищенными атрибутами
class Road:
    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width
        self._weight = weight
        self._thickness = thickness

    # создаем команду для расчета необходимого веса
    def mass(self):
        return \
            f"На полотно толщиной в {self._thickness}см. и площадью {(self._length * self._width) / 1000}" \
            f"кв.км. необходимо {(self._length * self._width * self._weight) * self._thickness / 1000} тонн асфальта."

# запрашиваем параметры атрибута в класс
road1 = Road(
    int(input("Введите ширину полотна в метрах: ")),
    int(input("Введите длину полотна в метрах: ")),
    int(input("Введите вес асфальта: ")),
    int(input("Введите высоту полотна в сантиметрах: ")))

# выполняем команду в классе
print(road1.mass())
