"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def dividion(*args):
    try:
        arg1 = int(input("Введите делиемое:"))
        arg2 = int(input("Введите делитель:"))
        res = arg1 / arg2
    except ValueError:
        return "Value error"
    except ZeroDivisionError:
        return "Делить на ноль нельзя"
    return res

    """
    if arg2 != 0:
    
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    """

print(f"Результат {round(dividion(),2)}")
