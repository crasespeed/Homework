with open('file_1.txt', 'w+') as my_f:
    text = input('Введите текст: ')
    while text:
        my_f.write(f"{text}\n")
        text = input('Введите текст: ')
        if not text:
            break
    my_f.seek(0)
    print(my_f.read())
