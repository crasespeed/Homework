import json
profit = {}
prof = 0
i = 0
with open('file_7.txt', 'r') as file_7:
    for line in file_7:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit[name] > 0:
            prof += profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
    pr = {'Средняя прибыль': round(prof_aver)}
    my_list = [profit, pr]
    print(f'Прибыль каждой компании:\n{my_list}')