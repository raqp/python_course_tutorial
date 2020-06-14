class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Store(Person):
    def __init__(self, name, surname, city):
        Person.__init__(self, name, surname, city)
        self.products = {}  # {"BOSH":{"icebox":{"price":300, "quantity": 5}
        self.account_balance = 0
        self.invoice_for_payment = 0

    def _add_product(self, model, title, price, quantity):
        if model in self.products:
            if title in self.products[model]:
                self.products[model][title]["quantity"] += quantity
            else:
                self.products[model][title] = {}
                self.products[model][title]["price"] = price
                self.products[model][title]["quantity"] = quantity
        else:
            self.products[model] = {}
            self.products[model][title] = {}
            self.products[model][title]["price"] = price
            self.products[model][title]["quantity"] = quantity

    def add_products(self):  # Добавляем товары в магазин
        number_of_products = int(input("Enter the number of products you want to add - "))
        for i in range(number_of_products):
            model = input("Model - ")
            title = input("Title - ")
            price = int(input("Price - "))
            quantity = int(input("Quantity - "))
            self._add_product(model, title, price, quantity)
            print("\n########################################\n")
        else:
            print("Products successfully entered the store")

    def show_products(self):  # Показываем какие товары доступны для покупки
        for i in self.products:
            print(f"Model: {i}")
            for j in self.products[i]:
                print(
                    f"\t{j}\n\t\tPrice: {self.products[i][j]['price']}$\n\t\tQuantity: "
                    f"{self.products[i][j]['quantity']}")

    def __total_amount(self, client):  # Считаем на какую сумму были куплены товары
        for model_1 in client.basket:
            for title_1 in client.basket[model_1]:
                if client.basket[model_1][title_1] > self.products[model_1][title_1]["quantity"]:
                    print(f" Unfortunately, the store is missing such an amount {title_1}")
                    continue
                self.invoice_for_payment = client.basket[model_1][title_1] * self.products[model_1][title_1]["price"]

        return self.invoice_for_payment

    def __balance_check(self, client):  # Проверка баланса клиента
        if self.__total_amount(client) > client.account_balance:
            return False
        return True

    def _delete_purchased_items(self, client):  # Удаляем купленные товары из списка товаров магазина
        if self.__balance_check(client):
            for i in client.basket:
                for j in client.basket[i]:
                    if client.basket[i][j] <= self.products[i][j]["quantity"]:
                        self.products[i][j]["quantity"] -= client.basket[i][j]
            return True
        return False

    def _balance_replenishment(self):  # Пополняем счет магазина
        self.account_balance += self.invoice_for_payment

    def _sale(self):  # Завершаем продажу
        self._balance_replenishment()
        self.invoice_for_payment = 0


class Client(Person):
    def __init__(self, name, surname, city, account_balance):
        Person.__init__(self, name, surname, city)
        self.account_balance = account_balance
        self.basket = {}  # {"BOSH":{"icebox":5}}
        self.spending_money = 0

    def add_in_basket(self, model, title, quantity):
        if model in self.basket:
            if title in self.basket[model]:
                self.basket[model][title] += quantity
            else:
                self.basket[model][title] = quantity
        else:
            self.basket[model] = {}
            self.basket[model][title] = quantity

    def buy(self, store):
        if store._delete_purchased_items(client=self):
            print("The purchase was successful.")
            print("#############RECEIPT################")

            for i in self.basket:
                print(f"Model: {i}")
                for j in self.basket[i]:
                    print(f"\t{j} : {self.basket[i][j]}")
            print(f"Paid : {store.invoice_for_payment}")

            self.account_balance -= store.invoice_for_payment
            self.spending_money += store.invoice_for_payment
            self.basket.clear()
            store._sale()
        else:
            print("Not enough funds on your balance")


Amazon = Store("Vitaliy", "Balyan", "Erevan")
client_1 = Client("Johnny", "Depp", "LA", 10000)
Amazon._add_product("BOSH", "Icebox", 300, 5)
Amazon.add_products()
client_1.add_in_basket("BOSH", "ABC", 5)
client_1.buy(Amazon)

Amazon.show_products()
