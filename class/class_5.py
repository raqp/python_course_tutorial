class Person:

    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    def __add__(self, other):
        self.pay += other
        return self.pay

    def __sub__(self, other):
        self.pay -= other
        return self.pay

    def __str__(self):
        return f"{self.name}, {self.job}"

    def __eq__(self, other):
        return self.pay == other.pay

    def __pow__(self, power, modulo=None):
        return self.pay ** power


john = Person("John", "developer", 400)
bob = Person("Bob", "teacher", 400)

print(john ** 2)
