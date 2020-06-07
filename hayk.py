class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Seller(Person):

    def __init__(self, name, surnem, city, sellers_car):
        Person.__init__(self, name, surnem, city)

        self.money = 0
        self.sold_car = {}
        self.sellers_car = sellers_car

    def finde_car_for_buyer(self, car_name, money):
        if car_name in self.sellers_car:
            price = self.sellers_car[car_name]
            if money >= price:
                self.money += money
                self.sold_car[car_name] = money
                del self.sellers_car[car_name]
                return True
        return False


class Buyer(Person):
    def __init__(self, name, surname, city, money):
        Person.__init__(self, name, surname, city)
        self.money = money
        self.spended_money = 0
        self.bought_car = {}

    def buy_car(self, seller, car_name, money):
        if seller.finde_car_for_buyer(car_name=car_name, money=money):
            self.spend_money(money)
            self.add_car(car_name, money)

    def spend_money(self, money):
        self.money -= money
        self.spended_money += money

    def add_car(self, car_name, money):
        self.bought_car[car_name] = money
