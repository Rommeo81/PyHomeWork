"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

# =========== решение задания 5.2 ==============

# Открываем файл в режиме чтения в кодировке utf-8 и выводим содержимое на экран.
my_file = open('test_2.txt', 'r', encoding="utf-8")
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
print(f'====='*5, "\n")

# Открываем файл в режиме чтения и считаем количество строк.
print(f'Количество строк в файле - {len(content)}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
print(f'====='*5, "\n")

# Открываем файл в режиме чтения и считаем количество символов в каждой строке и во всем тексте.
for i in range(len(content)):
    print(f'Количество символов в {i + 1}ой строке {len(content[i])}')
my_file = open('test_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'====='*5, "\n")
print(f'Общее количество слов - {len(content)}')
my_file.close()

