"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


def int_func(*agrs):
    word = input("Введите слова:")
    print(word.title())
    return


int_func()
