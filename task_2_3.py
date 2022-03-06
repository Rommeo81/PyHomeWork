# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict

# ----- решение задание 3 ------------

# Запрашиваем у пользователя месяц в виде целого числа
month = int(input("Enter the number of the month from 1 to 12: "))

# Формируем словарь месяцев с присвоением ключа
month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}

# Формируем словарь сезонов, где ключ - название сезона, а список - значения месяцев
season_dict = {"Winter": [1, 2, 12], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}

# Формируем список месяцев:
month_list = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")

# Ищем в картеже в списках месяц. Подбираем ключ этого значения.
# Выводим на экран значения из словаря и списка. Выводим на экран значения ключа списка.
if month in sum(season_dict.values(), []):
    for i in season_dict.items():
        if month in i[1]:
            print(f"{month} month is {month_dict[month]}. {month_dict[month]} is {i[0]}")
            print(f"{month} month is {month_list[month - 1]}. {month_dict[month]} is {i[0]}")
            break
else:
    print("Wrong month numer.")
