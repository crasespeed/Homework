from itertools import count
from itertools import cycle
for el in count(3):
    if el > 10:
        break
    print(el)
a = 0
for el in cycle('ABCDEFJ'):
    if a > 10:
        break
    print(el)
    a += 1
