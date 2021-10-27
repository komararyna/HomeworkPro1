class Intmag:
    def __init__(self, tov, price, size, colour, material):
        self.tov = tov
        self.price = price
        self.size = size
        self.colour = colour
        self.material = material

    def __str__(self):
        return f'{self.tov} ({self.price} грн, {self.size}, {self.colour}, {self.material})'


tovar_1 = Intmag('машинка', 29, '5 см', 'жёлтый', 'пластик')
tovar_2 = Intmag('кукла', 120, '25 см', 'красный', 'ткань')
tovar_3 = Intmag('вертолёт', 400, '15 см', 'чёрный', 'пластик')

print(tovar_1)
print(tovar_2)
print(tovar_3)


class Pokup:
    def __init__(self, name, surname, age, ph_num):
        self.name = name
        self.surname = surname
        self.age = age
        self.ph_num = ph_num

    def __str__(self):
        return f'{self.name} {self.surname}, {self.age}, {self.ph_num}'


cus_1 = Pokup('Ivan', 'Ivanov', 34, '0671234567')
cus_2 = Pokup('Petr', 'Petrov', 25, '0681234567')
cus_3 = Pokup('Maria', 'Markova', 27, '0961234567')

print(cus_1)
print(cus_2)
print(cus_3)


class Zakaz:
    def __init__(self, pers, *args):
        self.args = args
        self.pers = pers

    def summa(self):
        su = 0
        for item in self.args:
            su = su + item.price
        return 'Заказ на сумму: ' + str(su) + ' грн'

    def __str__(self):
        res = ''
        for item in self.args:
            res = res + str(item) + '; '
        return f'Покупатель: {self.pers}; Товары: {res}'


zak_1 = Zakaz(cus_1, tovar_2, tovar_3)
zak_2 = Zakaz(cus_2, tovar_1, tovar_2)
zak_3 = Zakaz(cus_3, tovar_1, tovar_2, tovar_3)

print(zak_1)
print(zak_1.summa())
