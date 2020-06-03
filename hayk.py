enter_name = input("Please  enter Your name - ")
enter_password = input("Please  enter Your password - ")


class Person:

    def __init__(self, name, job, points, pay, password):
        self.name = name
        self.job = job
        self.points = points
        self.__pay = pay
        self.__password = password
        self.__info_dict = {self.name: [self.job, self.__pay, self.points, self.__password]}


class Points(Person):

    def __init__(self, name, job, points):
        Person.__init__(self, name, job, points, pay=None, password=None)

    def add_points(self, name, job, add_new_points, chack=False):
        self.name = name
        self.job = job

        if chack and add_new_points:
            global info_dict
            info_dict[self.name][2] += add_new_points


# class Accountant(Person):
#   poxelu ban ka  boss_accountant = Person(input("Please  Enter Your Name - "), "accountant",
#                              password=input("Please  Enter yor password - ")
#                              , points=None, pay=None, )
#     def __init__(self,name,job,point,pay):
#         Person.__init__(self,name,job,point,pay,password=None)
#         self.name = name
#         self.point = point
#         self.pay = pay
#     if boss_accountant.name == "Jone" and boss_accountant.password == "Yes":
#         def new_pay(self,new_pay):
#             global info_dict
#             if info_dict[self.name][2] > 4:
#                 info_dict[self.name][1] += new_pay
bob = Person("Bob", "developer", 0, 100, "BOB")

# if enter_name in info_dict and info_dict[enter_name][3] == enter_password:
#     print(*info_dict[enter_name])
