class MyException(Exception):

    def division_func(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f'{a} / {b} -> на ноль делить нельзя!\n')
        else:
            print(f'{a} / {b} = {res} \n')


m_e = MyException()

m_e.division_func(1, 2)
m_e.division_func(1, 0)
m_e.division_func(-1, 3)
m_e.division_func(0, 4)