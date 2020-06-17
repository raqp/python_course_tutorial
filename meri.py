class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Seller(Person):
    def __init__(self, name, surname, products, account):
        Person.__init__(self, name, surname)
        self.products = products
        self.account = account

    def getTheCost(self, tech):
        return self.products[tech]

    def printTheCost(self, tech):
        print(tech, self.products[tech])

    def addToTheAccount(self, tech):
        self.account += self.getTheCost(tech)

    def deleteTheTech(self, tech):
        del self.products[tech]

    def extandTheCollection(self, new_tech, new_cost):
        if self.account >= new_cost:
            self.account -= new_cost
            self.products[new_tech] = new_cost


class Buyer(Person):
    def __init__(self, name, surname, money):
        Person.__init__(self, name, surname)
        self.money = money
        self.basket = {}

    def buyTheTech(self, tech, seller):
        if self.money >= seller.getTheCost(tech):
            self.money -= seller.getTheCost(tech)
            seller.addToTheAccount(tech)
            seller.deleteTheTech(tech)
        else:
            print(f"{self.name} doesn't have enough money,sorry(((")

    def getTheMoney(self):
        return self.money

    # def addToBasket(self, tech, seller):
    #     self.basket[tech] = seller.getTheCost(tech)
    #     self.buyTheTech(tech, seller)
    #
    # def returnTheBasket(self):
    #     return self.basket


s = Seller("Vazgen", "Hambardzumyan", {"TV": 500, "PC": 600, "Mixer": 80}, 200)
b = Buyer("Gurgen", "Hakobyan", 500)

s.extandTheCollection("Iron", 400)
b.buyTheTech("TV", s)
print(b.getTheMoney())

# b.addToBasket("TV", s)
# b.addToBasket("PC", s)
# print(b.returnTheBasket())
