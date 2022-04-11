"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

# =========== решение задания 5.1 ==============

# создаем стартовый список
my_list = []

# Собираем весь текст в список.
while True:
    line = input("Enter anything: ")
    if line == '':  # если ничего не будет введено, то выводим все, что написали на экран и переходим к with.
        print(my_list)
        exit()

    # добавляем перенос на новую строку при добавлении еще текста и присоединяем в список его.
    else:
        newline = line + '\n'
        my_list.append(newline)

    # Открываем файл на запись. При этом удаляем содержимое файла, если было. Если файла нет, создается новый.
    # Все записываем в файл, выполняя части "if" (сбора текста)
    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)