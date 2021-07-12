from itertools import count
from math import factorial
def generator():
    for el in count(1):
        yield factorial(el)
gen = generator()
a = 0
for i in gen:
    if a <= 10:
        print(i)
        a += 1
    else:
        break
