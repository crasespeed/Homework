trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r') as file:
    content = file.read().splitlines()
    for i in content:
        i = i.split(' ', 1)
        new_file.append(trans[i[0]] + ' ' + i[1])
    print(new_file)

with open('file_4_1.txt', 'w',) as file:
    file.writelines('\n'.join(new_file))

