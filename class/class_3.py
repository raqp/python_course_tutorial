class Person:

    def __init__(self, name, profession, salary, height=175):
        self.name = name
        self.profession = profession
        self.salary = salary
        self.height = height

    def __str__(self):
        return f"Hello, my name is {self.name}"

    def get_person_info(self):
        print(f"Hello my name is {self.name}.\nI am {self.profession}.\nI earn {self.salary}")

    def print_all(self):
        print(f"Name: {self.name}\nProfession: {self.profession}\nSalary: {self.salary}")


bob = Person(name="Bob", profession="developer", salary="200$")
x = str(bob)
print(x)