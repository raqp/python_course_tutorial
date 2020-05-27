class Person:

    def __init__(self, name, phone, pay):
        self.name = name
        self._phone = phone
        self.__pay = pay

    def change_phone_number(self, new_phone_number):
        self._phone = new_phone_number

    def _person_phone(self):
        return self._phone

    def get_person_pay(self):
        return self.__pay

    def __change_person_pay(self, new_pay):
        self.__pay += new_pay

    def change_pay(self, x):
        if x < 1000:
            self.__change_person_pay(x)
        else:
            print("ALERT")


john = Person("John", 37494202020, 500)
