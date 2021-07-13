with open('file_2.txt', 'r') as file:
    text = file.readlines()
    print(f'Количество строк: {len(text)}')
    for i in range(len(text)):
        print(f'В строке слов: {len(text[i].split())}')