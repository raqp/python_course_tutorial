class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Seller(Person):
    def __init__(self, name, surname, city, product):
        Person.__init__(self, name, surname, city)
        self.product = product
        self.sold_tech = {}
        self.money = 0

    def sel_item(self, quantity=0, tech_model=None, tech_name=None, basket=None):
        # {"BOSH": {"sarnaran": 3, "washing machine": 2}}
        sp_money = 0
        # if tech_model in self.product and tech_name in self.product[tech_model] and self.product["quantity"]:
        if basket:
            for model in basket:
                for name in basket[model]:
                    self.product[model][name]["quantity"] -= basket[model][name]
                    sp_money += self.product[model][name]["price"] * basket[model][name]
        else:
            self.product[tech_model][tech_name]["quantity"] -= quantity
            sp_money += self.product[tech_model][tech_name]["price"] * quantity
        self.take_money(sp_money)
        return sp_money

        #     self.abc(tech_model, tech_name, quantity)
        #     self.take_money(self.product[tech_model][tech_name]["price"])
        #     return True
        # else:
        #     return False

    def __take_money(self, money):
        self.money += money

    def take_money(self, money):
        self.__take_money(money)


class Buyer(Person):
    def __init__(self, name, surname, city, money, card_money):
        Person.__init__(self, name, surname, city)
        self.money = money
        self.card = card_money
        self.shopping_basket = {}
        self.spending_money = 0

    def selling(self, seller, tech_model=None, tech_name=None, quantity=1):
        if self.shopping_basket:
            sp_money = seller.sel_item(basket=self.shopping_basket)
            self.clear_shopping_basket()
        else:
            sp_money = seller.sel_item(tech_model=tech_model, tech_name=tech_name, quantity=quantity)
        self.spend_money(sp_money)

        # if seller.sel_item(tech_name, quantity):
        #     self.shopping_basket[tech_name] = quantity
        #     del seller.sel_item[tech_name]
        #     print("The purchase was successful!")
        # else:
        #     print("You have been denied a purchase!")

    def spend_money(self, money, card_pay=False):
        if card_pay or self.money < money:
            self.card -= money
        else:
            self.money -= money
        self.spending_money += money

    def add_item_in_basket(self, tech_model, tech_name, quantity):
        # {"BOSH": {"sarnaran": quantity, "washing machine": quantity}}
        if tech_model in self.shopping_basket:
            if tech_name in self.shopping_basket[tech_model]:
                self.shopping_basket[tech_model][tech_name] += quantity
            else:
                self.shopping_basket[tech_model][tech_name] = quantity
        else:
            self.shopping_basket[tech_model] = {}
            self.shopping_basket[tech_model][tech_name] = quantity

    def clear_shopping_basket(self):
        self.shopping_basket.clear()


seller_1 = Seller("Greg", "House", "Yerevan",
                  {"BOSH": {"washing machine": {"price": 300, "quantity": 10},
                            "sarnaran": {"price": 400, "quantity": 15}}})

buyer_1 = Buyer("Will", "Smith", "Moscow", 3000, 2000)
buyer_1.add_item_in_basket("BOSH", "sarnaran", 2)
buyer_1.add_item_in_basket("BOSH", "washing machine", 3)
buyer_1.selling(seller_1)
# buyer_1.selling(seller_1, tech_model="BOSH", tech_name="sarnaran", quantity=5)
print(seller_1.money)
print(seller_1.product)
print(buyer_1.money)

