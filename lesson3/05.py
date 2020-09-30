"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
 Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_func():
    temp = 0
    ex = False
    while not ex:
        num = input("Введите сторку чисел разделенную пробелами или Q для выхода").split()

        res = 0
        for i in range(len(num)):
            if num[i] == 'q' or num[i] == 'Q':
                ex = True
                break
            else:
                res = res + int(num[i])
        temp = temp + res
        print(f"Текущая сумма {temp}")
    print(f"Твоя финальная сумаа {temp}")


my_func()
