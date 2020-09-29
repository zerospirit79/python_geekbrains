# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

qty = int(input("Введите количество элементов: "))
new_list = []
i = 0
element = 0
while i < qty:
    new_list.append(input("Введите элемент списка: "))
    i += 1

for i in range(int(len(new_list)/2)):
    new_list[element], new_list[element + 1] = new_list[element + 1], new_list[element]
    element += 2
print(new_list)
