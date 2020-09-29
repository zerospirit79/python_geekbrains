# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print("hex(17) type is", type(hex(17)))
a = 5
b = 13
c = a & b
# print(bin(a), bin(b), bin(c), c)
print("a & b type is",type(c))
# print(bin(a), bin(b), bin(a | b), (a | b))
# print(bin(a), bin(b), bin(a ^ b), (a ^ b))
z = [1, 2, 3, 4, 5]
f = ("one", "two", "three", "four")
s = {a, 1, b, 3, f}
frosen_s = frozenset(s)
# print(s)
print(z, "type is", type(z))
print(f, "type is",type(f))
print(s, "type is",type(s))
print(frosen_s, "type is",type(frosen_s))
new_object = {"name": "Pavel", "age": 41}
print(new_object, "type is",type(new_object))
