"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open(r"02.txt", "r")
content = my_file.read()
print(f"Содержимое: \n {content}")
my_file = open(r"02.txt", "r")
content_lines = my_file.readlines()
print(f"Колличество строк: {len(content_lines)}")
my_file = open(r"02.txt", "r")
content_words = my_file.readlines()
for i in range(len(content_words)):
    line = content_words[i].split()
    word = len(line)
    print(f"Колличество слов в строке - {word} в строке - {i}")

my_file.close()
