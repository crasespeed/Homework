def s_calc(*args):
    try:
        arg1 = int(input("Введите первое число "))
        arg2 = int(input("Введите второе число "))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    return res
print(f'Рузультат {s_calc()}')