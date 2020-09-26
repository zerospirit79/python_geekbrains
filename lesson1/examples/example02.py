# password = input("Введите пароль >>>")
# original_password = "correct"
# if original_password == password:
#     print("Correct")
# else:
#     print("Incorrect")
#
age = int(input("Введите ваш возраст >>>"))
if age >= 14:
    print("паспорт можно получать")
    if 20 <= age < 45:
        print("паспорт можно поменять")
elif age < 1:
    print("Custom")
else:
    print("пока рано")