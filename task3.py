# Задание 3 ----------------------------
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print("----- lesson 1, task 3 -----")
n = input("Enter integer number 'n': ")
while n < '0':
    n = input("Enter integer number 'n', more than 0: ")
print("Result 'n + nn + nnn' is", int(n) + int(n + n) + int(n + n + n))
print("=====================================")