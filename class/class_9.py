class A:

    def power(self, a, b):
        return a ** b

    def mult(self, a, b):
        return a * b


class B(A):

    def add(self, a, b):
        return a + b

    def power(self):
        return "Hello"


x = B()
print(x.power())
