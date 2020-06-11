class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Seller(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self.money = 0
        self.products = {"iron": 50, "TV": 700, "laptop": 1000}

    def answer_to_buyer(self, question):
        if question in self.products:
            return question + " is worth " + str(self.products[question])
        else:
            return "This product isn't available"

    def sell_product(self, product_name, count):
        sp_money = 0
        sp_money += self.products[product_name] * count
        self.take_money(sp_money)
        return sp_money

    def __take_money(self, money):
        self.money += money

    def take_money(self, money):
        self.__take_money(money)


class Buyer(Person):
    def __init__(self, name, age, amount_of_money):
        Person.__init__(self, name, age)
        self.amount_of_money = amount_of_money

    @staticmethod
    def question_to_seller(seller, question):
        message = seller.answer_to_buyer(question)
        print(message)

    def buy_product(self, seller, product_name, count=1):
        sp_money = seller.sell_product(product_name, count)
        self.spend_money(sp_money)

    def __spend_money(self, money):
        self.amount_of_money -= money

    def spend_money(self, money):
        self.__spend_money(money)


gabe = Seller("Gabe", 57)
player = Buyer("Player", "25", 5000)

player.question_to_seller(seller=gabe, question="TV")
player.buy_product(seller=gabe, product_name="TV", count=2)
player.buy_product(seller=gabe, product_name="laptop", count=2)
print(player.amount_of_money)
print(gabe.money)

