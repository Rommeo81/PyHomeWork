"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

# ====== решение задания 4.1  ============

# подключаем модуль sys c оператором argv для забора данных из командной строки
from sys import argv

# Создаём функцию для вычислений и вывода результата. В случае ошибки выводим сообщение.
def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Total salary - {time * rate + bonus}")
    except ValueError:
        print("Enter 3 number: work time, rate and bonus. ")

# выполняем созданную функцию
salary()

# вводим данные через терминал в командной строке python:
# python C:/Users/romme/Documents/PyHomeWork/PyHomeWork/lesson_4/task_4_1.py 98 65 98
# для примера использовал прямой адрес на файл
