"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

desc = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open(r'03_1.txt', 'r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(desc[i[0]] + ' ' + i[1])
        print(new_file)
with open('file_03.txt', 'w') as file_obj_03:
    file_obj_03.writelines(new_file)