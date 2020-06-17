class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Seller(Person):
    def __init__(self, name, surname, technica, money):
        Person.__init__(self, name, surname)
        self.technica = technica  # dict {boch:{price: 500, quantity: 5}}
        self.money = money

    def add_new_technica(self, name, price, quantity):
        self.technica[name] = {}
        self.technica[name]["price"] = price
        self.technica[name]["quantity"] = quantity

    def select_technica(self, name, quantity, money):
        if name in self.technica and quantity <= self.technica[name]["quantity"] \
                and money >= self.technica[name]["price"] * quantity:
            return True
        return False

    def buy_technica(self, name, money, quantity):

        if name in self.technica and money >= self.technica[name]["price"] \
                and self.technica[name]["quantity"] >= quantity:
            self.money += money
            self.technica[name]["quantity"] -= quantity
            print(':)')
            return True
        else:
            print(":(")

    def all_work(self, name, money, quantity, box=False, buy=False, add=False):
        if box:
            self.select_technica(name, quantity, money)
        elif buy:
            self.buy_technica(name, quantity, money)
        elif add:
            self.add_new_technica(name, quantity, money)
        else:
            print("Orient yourself ։(")


class Buyer(Person):
    def __init__(self, name, surname, money, ):
        Person.__init__(self, name, surname)
        self.bought = {}
        self.shop_box = {}  # name ,quantity:,money
        self.money = money
        self.sp_money = 0

    # def add_shop_box(self, seller, name, quantity, money):
    #     if seller.select_texnik(name):
    #         self.shop_box[name] = [money, quantity]
    #
    # def buy_texnika(self, seller, name, money, quantity):
    #     if seller.buy_technica(name, money, quantity):
    #         self.bought[name] = [money * quantity, quantity]
    #         self.sp_money += quantity * money

    def all_woke_buyer(self, seller, name, quantity, money, add=False, buy=False, box=False):
        if add and seller.select_texnik(name, quantity, money):
            self.shop_box[name] = {}
            self.shop_box[name]['quantity'] = quantity
            self.shop_box[name]['price'] = money

        if buy and seller.buy_technica(name, money, quantity):
            self.bought[name] = {}
            self.bought[name]['quantity'] = quantity
            self.bought[name]['price'] = money * quantity
            self.sp_money += money * quantity

        if box:
            total_money = 0
            for money in self.shop_box:
                total_money += money['price']
            if self.money >= total_money:
                print("You can buy all :)")
