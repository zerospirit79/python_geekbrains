from typing import Any, Union

a = int(input("Ввведите результат пробежки в первый день: "))
b = int(input("Введите результат пробежки, который хотите достигнуть: "))
days = 1

while a < b:
    a *= 1.1
    days += 1
print(f"Вы достигните результата на {days} день")
