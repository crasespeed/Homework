def sal():
    try:
        time = float(input('Время работы '))
        money = float(input('Ставка '))
        bonus = float(input('Премия '))
        res = (time * money) + bonus
        print(f'Заработная плата составит  {res}')
    except ValueError:
        return print('Not a number')
sal()