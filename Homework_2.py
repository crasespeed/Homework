                    #  №1
def task1():
    list = [-100, 100.5, 'False', True, None]
    for el in list:
        print(type(el))

                    #  №2
def task2():
    list = int(input("Введите количество элементов: "))
    num = []
    i = 0
    while i < list:
        num.append(input("Введите значение: "))
        i += 1
    for el in range(int(len(num)/2)):
            num[el], num[el + 1] = num [el + 1], num[el]
            el += 2
    print(num)
                    #  №3
def tas3():
    dict = ['Зима', 'Весна', 'Лето', 'Осень']
    month = int(input("Введите номер месяца "))
    if  month in [12,1,2,]:
         print(dict[0])
    elif month in [3,4,5,]:
        print(dict[1])
    elif month in [6,7,8,]:
        print(dict[2])
    elif month in [9,10,11,]:
        print(dict[3])
    else:
        month > 12
        print('В году двеннадцать месяцев!')

                    #  №4
def task4():
    word = input('Введите несколько слов ')
    word = str.split(word)
    for num, el in enumerate(word):
        if len(str(word)) <= 10:
            print(num, el)
        else:
            len(str(word)) <= 10
            print(num, el [0:10])

                    #  №5
def task5():
    num = int(input("Введите цифру: "))
    list = [9, 7, 5, 3, 1 ]
    a = list.count(num)
    for el in list:
        if a > 0:
            b = list.index(num)
            list.insert(b+a, num)
            break
        else:
            if num > el:
                c = list.index(el)
                list.insert(c, num)
                break
            elif num < list[len(list) - 1]:
                list.append(num)
    print(list)

