class Person:

    def initialization(self, name, profession, salary, height):
        self.name = name
        self.profession = profession
        self.salary = salary
        self.height = height

    def print_info(self):
        print(f"Hello my name is {self.name}.\nI am {self.profession}.\nI earn {self.salary}.")


bob = Person()
bob.initialization(name="Bob", profession="developer", salary="175$", height=176)
john = Person()
john.initialization(name="John", profession="teacher", salary="50$", height=153)
john.age = 29
john.profession = "doctor"
john.salary = "800$"
