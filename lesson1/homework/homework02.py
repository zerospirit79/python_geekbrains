time_second = int(input("Введите число секунд >>>"))

seconds = time_second % (24 * 3600)
hours = time_second//3600
seconds %= 3600
minutes = seconds//60
seconds %= 60

print(f"Вы ввели время {hours}:{minutes}:{seconds}")