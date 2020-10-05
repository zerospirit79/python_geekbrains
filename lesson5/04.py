"""
Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summa():
    try:
        with open('04.txt', '+w') as my_file:
            numbers = input("Введите числа через пробел: \n")
            my_file.writelines(numbers)
            my_numbers = numbers.split()

            print(sum(map(int, my_numbers)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Вы ввели неверное число")


summa()
