"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

# ----- решение задание 2 -----

# создаем функцию my_func и указываем аргументы
def my_func(name, surname, year, city, email, phone):
    return print(f"{name} {surname} {year} {city} {email} {phone}")   # возвращаем значения строкой

# задаем именные аргументы
my_func(city="Wroclaw", year=1981, surname="Menshchykau", name="Roman", email="mail@mail.com",
        phone="+48 123-456-789")
