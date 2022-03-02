# Задание 2 ----------------------------
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print("----- lesson 1, task 2 -----")
timeseconds = int(input("Enter time in seconds: "))
days = timeseconds // 86400
hours = timeseconds // 3600 - days * 24
minutes = timeseconds // 60 - days * 24 - hours * 60
seconds = timeseconds % 60
print(f"{timeseconds} seconds = {days:02} days, {hours:02} hours, {minutes:02} minutes, {seconds:02} seconds")
print("=====================================")