# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_date = int(input("Введите номер месяца от 1 до 12: "))
seasone = {1: "winter", 2: "spring", 3: "summer", 4: "autumn"}

if month_date == 12 or month_date == 1 or month_date == 2:
    print(seasone.get(1))
elif month_date == 3 or month_date == 4 or month_date == 5:
    print(seasone.get(2))
elif month_date == 6 or month_date == 7 or month_date == 8:
    print(seasone.get(3))
else:
    print(seasone.get(4))