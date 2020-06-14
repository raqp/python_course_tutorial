class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Seller(Person):
    def __init__(self, name, surname, technica, money):
        Person.__init__(self, name, surname)
        self.technica = technica  # dict {boch:[pricr,quantity], lg:[100, 50]}
        self.money = money

    def add_new_technica(self, name, price):
        self.technica[name] = price

    def select_technica(self, name, quantity, money):
        if name in self.technica and quantity <= self.technica[name][1] and money >= self.technica[name][0]:
            return True
        return False

    def buy_technica(self, name, money, quantity):
        if name in self.technica and money >= self.technica[name][0] and self.technica[name][1] >= quantity:
            self.money += money
            self.technica[name][1] -= quantity
            print(':)')
            return True
        else:
            print(":(")


class Buyer(Person):
    def __init__(self, name, surname, money):
        Person.__init__(self, name, surname)
        self.bought = {}
        self.shop_box = {}  # name ,quantity:,money
        self.money = money
        self.sp_money = 0

    def add_shop_box(self, seller, name, quantity, money):
        if seller.select_texnik(name):
            self.shop_box[name] = [money, quantity]

    def buy_texnika(self, seller, name, money, quantity):
        if seller.buy_technica(name, money, quantity):
            self.bought[name] = [money * quantity, quantity]
            self.sp_money += quantity * money

    def shop_box_(self):
        print(self.shop_box)
        total_money = 0

        for i in self.shop_box:
            total_money += self.shop_box[i][0]
        return total_money
