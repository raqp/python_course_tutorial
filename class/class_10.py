# MRO


class A:

    def __init__(self, a):
        self.name = "A"
        self.a = a

    # def __str__(self):
    #     return self.name

    def my_function(self, x, y):
        return x * y


class B:

    def __init__(self, b):
        self.name = "B"
        self.b = b

    def my_function(self, x, y):
        return x + y


class C(A, B):

    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)
        self.name = "C"


some_object = C("hello", "John")
print(C)
