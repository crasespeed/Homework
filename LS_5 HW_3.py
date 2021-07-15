with open('file_3.txt', 'r', encoding='utf-8') as file:
    salary = []
    name = []
    list = file.read().split()
for i in list:
    i = i.split()
if i [1] < 20000:
    name.append(i[0])
    salary.append(i[1])
print(f'Оклад меньше 20.000 {name}, средний оклад {sum(map(int, salary)) / len(salary)}')