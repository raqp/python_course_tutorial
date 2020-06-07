class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Buyer(Person):
    def __init__(self, name, surname, city, money):
        Person.__init__(self, name, surname, city)
        self.money = money
        self.spended_money = 0
        self.bought_cars = []

    def buyers_choice(self, seller, choice, price):
        seller.sale_cars(choice, price)
        self.bought_cars.append(choice)
        self.spended_money += price


class Seller(Person):
    def __init__(self, name, surname, city):
        Person.__init__(self, name, surname, city)
        self.car_park = ["bmw", "mercedes"]
        self.sold_cars = {}
        self.money = 0

    def sale_cars(self, choice, price):
        self.car_park.remove(choice)
        self.sold_cars[choice] = price
        self.money += price


mihran = Seller("Mihran", "Khachatryan", "Yerevan")
rafo = Buyer("Rafik", "Parsyan", "Sisian", 100000)

rafo.buyers_choice(mihran, "bmw", 95000)

print(mihran.car_park)
print(mihran.money)
print(rafo.bought_cars)







