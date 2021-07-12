from functools import reduce
list = [el for el in range(100, 1001) if el % 2 == 0]
print(list)
def func(num, el):
    return num * el
print(reduce(func, list))
