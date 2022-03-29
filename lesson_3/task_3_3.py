"""Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов"""

# ----- решение задание 3 (первый вариант решения) -----

# просим ввести аргументы
arg1 = int(input("Enter 1st argument: "))
arg2 = int(input("Enter 2nd argument: "))
arg3 = int(input("Enter 3rd argument: "))

# Описываем действия my_func
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

# Задаем позиции аргументов и выводим результат функции my_func
print(f'Sum - {my_func(arg1, arg2, arg3)}')
print("=========" * 10)

# ----- решение задание 3 (вариант решения) -----

arg1 = int(input("Enter 1st argument: "))
arg2 = int(input("Enter 2nd argument: "))
arg3 = int(input("Enter 3rd argument: "))

# Описываем действия my_func
def my_func(arg1, arg2, arg3):
    return print(f"Sum is {arg1 + arg2 + arg3 - min(arg1, arg2, arg3)}")

# Задаем позиции аргументов и выводим результат функции my_func
my_func(arg1, arg2, arg3)
