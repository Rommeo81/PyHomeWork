"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль"""

# ----- решение задание 2 -----

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Y не может быть нулем"
    except ValueError:
        return "Введите только числа"

    # просим ввести позиционные целочисленные параметры и выводим результат my_func
print(my_func(int(input("Введите значение X = ")), int(input("Введите значение Y = "))))
