class Person:

    def __init__(self, name, job, experience, position):
        self.name = name
        self.job = job
        self.experience = experience
        self.position = position


class Accountant(Person):

    def __init__(self, name, experience, position, pay, emp_pay_permission=False):
        Person.__init__(self, name, "accountant", experience, position)
        self.emp_pay_permission = emp_pay_permission
        self.pay = pay

    @staticmethod
    def __change_employee_pay(employee, new_pay):
        employee.pay = new_pay

    def change_employee_pay(self, employee, some_pay):
        if self.emp_pay_permission:
            if some_pay / employee.pay < 2:
                new_pay = self._income_tax(some_pay)
                self.__change_employee_pay(employee=employee, new_pay=new_pay)
                print(f"{employee.name} pay successfully changed.")
            else:
                print("Failed to change employee pay.")
        else:
            print("Permission denied.")

    @staticmethod
    def _income_tax(pay):
        return pay - pay * 0.23


class Employee(Person):

    accountant = Accountant("John", 2, "senior", 500, emp_pay_permission=True)

    def __init__(self, name, job, experience, position, department, pay):
        Person.__init__(self, name, job, experience, position)
        self.department = department
        self.pay = pay
        self.slave_list = []

    def change_department(self, new_department):
        self.department = new_department
        print(f"{self.name} successfully changed department. New department is {self.department}")

    def change_my_pay(self, new_pay):
        self.accountant.change_employee_pay(self, new_pay)


bob = Employee("Bob", "developer", 1, "juniora", "MyDev", 300)
bob.change_my_pay(500)
bob.change_department("ABC")