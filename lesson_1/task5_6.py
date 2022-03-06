# Задание 5 и 6 ----------------------------
# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

print("----- lesson 1, task 5 and 6  -----")
revenue = float(input("Enter the revenue in USD: "))
costs = float(input("Enter the costs in USD: "))
profit = revenue - costs    # Задаем значение переменной прибыли, как разницу между выручкой и затратами.

# Описываем действия, если фирма сработала с прибылью
if profit > 0:
    print(f"Good job! You have a profit {profit:.2f} USD.")
    print(f"Your profitability is {profit / revenue * 100:.2f}%")
    personal_number = int(input("Now we will calculate profit per employee. Enter number employee in your firm: "))
    print(f"Profit {profit / personal_number:.2f} per employee in USD.")

# Описываем действия, если фирма сработала в убыток
elif profit < 0:
    print(f"Sorry, you have losses {profit} USD.")

# Описываем действия, если фирма  сработала с прибылью равной нулю
else:
    print(f"You have {profit} USD profit. Try in hext period work better!")

print("=====================================")