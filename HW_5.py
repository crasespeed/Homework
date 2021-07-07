def sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('введите числа через пробел или A - для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if  number[el] == 'A':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел {sum_res}')
sum()