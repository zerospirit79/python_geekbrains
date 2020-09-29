# value = 10 + 5
# print(value)
# value = "test"
# print(value)
# num = 0.1 + 0.2
# if num == 0.3:
#     print("Yes\t")
#     print(num)
# else:
#     print("No\t")
#     print(num)
#
# cars = "123"
# print(cars[::-1])

# nat = input("введи:")
# nat = list(set(nat))
# str_nat = ''.join(nat)
# print(str_nat)

nat = set(input("Введи:"))
unic_nat = (list(nat))
str_nat = ''.join(nat)
print(str_nat)
for x in unic_nat:
    x = int(x)+1
print(x)