class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Seller(Person):

    def __init__(self, name, surname, city, cars):
        Person.__init__(self, name, surname, city)
        self.car_park = cars
        self.sold_car = {}
        self.money = 0

    def print_info(self):
        for i in self.car_park:
            print(f'{i}:\n  Кол-во: {self.car_park[i]["count"]}\n  Цена: {self.car_park[i]["price"]}', end="\n")

    def __finish(self, buyer, car_name, money):
        if car_name in buyer.bought_cars:
            buyer.bought_cars[car_name] += 1
        buyer.spended_money += money
        self.car_park[car_name]["count"] -= 1
        self.money += money
        if car_name in self.sold_car:
            self.sold_car[car_name]["count"] += 1
            self.sold_car[car_name]["price"] += money
        else:
            self.sold_car[car_name] = {}
            self.sold_car[car_name]["count"] = 1
            self.sold_car[car_name]["price"] = money

    def __confirmation(self, car_name, money):
        if self.car_park[car_name]["count"] > 0:
            if money >= self.car_park[car_name]["price"]:
                return True
            else:
                print("Вам отказано в покупке данного автомобиля!")
        else:
            print("Автомобиль данной марки отсутсвует на аукционе!")
            return False

    def sale(self, buyer, car_name, money):
        if self.__confirmation(car_name, money):
            self.__finish(buyer, car_name, money)
            print("Покупка автомобиля прошла успешно!")


class Buyer(Person):

    def __init__(self, name, surname, city, money):
        Person.__init__(self, name, surname, city)
        self.bought_cars = {}
        self.money = money
        self.spended_money = 0

    def buy_car(self, car_name, money, seller):
        seller.sale(self, car_name, money)


seller_1 = Seller("John", "Carter", "LA",
                  {"Mercedes": {"count": 3, "price": 5000}, "BMW": {"count": 5, "price": 6000},
                   "Audi": {"count": 6, "price": 4000},
                   "SSC_Tuatara": {"count": 7, "price": 9000}})

buyer_1 = Buyer("Gabe", "Newell", "Seattle", 270000)
buyer_1.buy_car("Mercedes", 6000, seller_1)
buyer_2 = Buyer("Bob", "Bobyan", "Yerevan", 45000)
print(buyer_1.spended_money)
# a.buy_car(car_name="SSC_Tuatara", money=10000 )
