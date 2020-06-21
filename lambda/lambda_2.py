# def my_function(x):
#     return lambda y: x ** y


def my_function(x):
    def second_function(y):
        return x ** y
    return second_function


a = my_function(2)
# print(a)
print(a(5))
print(a(2))
print(a(6))
