class Person:
    name = "Bob"
    age = 28
    profession = "developer"
    salary = "150$"

    def print_info(self):
        print("Hello, my name is", self.name)


bob = Person()
# bob.print_info()


john = Person()
john.name = "John"
john.age = 20
john.salary = "300$"
john.height = 153
print(john.height)



