"""
Создать класс TrafficLight (светофор).
    ● определить у него один атрибут color (цвет) и метод running (запуск);
    ● атрибут реализовать как приватный;
    ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    ● продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
        третьего (зелёный) — на ваше усмотрение;
    ● переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    ● проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт
"""


# ====== решение задания 6.1 ============

# импортируем модуль time, в нем есть функция sleepl, для задержки выполнения цикла
import time

# создаем класс светофор
class TrafficLight:
    # создаем приватный атрибут с названиями цветов светофора
    __color = ["Красный", "Желтый", "Зеленый"]

    # создаем команду для отображения цветов, между выводом новой фразы вставляем задержку в секундах
    # используем "\r\033[31m" - для подкрашивания текста цветом и ', end=" "' для перехода в начало строки
    def running(self):
        while True:
            print(f"\r\033[31m{self.__color[0]}", end=" ")
            time.sleep(7)
            print(f"\r\033[33m{self.__color[1]}", end=" ")
            time.sleep(2)
            print(f"\r\033[32m{self.__color[2]}", end=" ")
            time.sleep(7)
            print(f"\r\033[33m{self.__color[1]}", end=" ")
            time.sleep(2)

# запускаем класс и запускаем команду
trafficlight = TrafficLight()
trafficlight.running()
