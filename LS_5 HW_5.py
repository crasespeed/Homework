with open("file_5.txt", "w+") as file_5:
    text = input('Введите числа через пробел: ')
    file_5.writelines(text)
    num = text.split()
print(sum(map(float, num)))
