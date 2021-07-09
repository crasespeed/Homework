list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список, {list}')
my_list = [el for num, el in enumerate(list) if list[num-1] < list[num]]
print(f'Новый список {my_list}')
