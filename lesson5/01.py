"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open(r"01.txt", "w")

if my_file.writable():
    strings = ["My\n", "new\n", "text\n"]
    my_file.writelines(strings)
else:
    print("Can't write")

my_file.close()