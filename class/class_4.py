#  machine count


class Car:
    count = 0

    def __init__(self, model, color):
        self.model = model
        self.color = color
        Car.count += 1

    def crash(self):
        Car.count -= 1


bmw = Car("BMW", "Black")
audi = Car("Audi", "Black")
mercedes = Car("Mercedes", "White")
print(bmw.count)
Car.count -= 1
print(bmw.count)

