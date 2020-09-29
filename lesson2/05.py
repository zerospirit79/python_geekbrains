# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
num = int(input("Введите число: "))


def listing(a, value):
    max_value = max(a)
    if value > max_value:
        a.insert(0, value)
    elif value in a:
        a.insert(a.index(value), value)
    else:
        a.append(value)


listing(my_list, num)
my_list.sort()
my_list.reverse()
print(my_list)

