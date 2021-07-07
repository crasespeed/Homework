name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите возвраст: '))
city = input('Введите город: ')
email = input('Введите email: ')
telephone = input('Введите телефон: ')
def my_func (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(name, surname, year, city, email, telephone)