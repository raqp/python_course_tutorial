class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Cat(Animal):

    def __init__(self, name, age, height):
        Animal.__init__(self, name=name)
        self.age = age
        self.height = height


class Dog(Animal):

    def __init__(self, x):
        Animal.__init__(self, name=x)


cat_a = Cat("Tom", 4, 20)
print(cat_a.name)

dog_a = Dog("Bobby")
dog_b = Dog("Chalo")
