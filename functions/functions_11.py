b = 10


def my_function(x, a=[]):
    # print(i for i in globals() if not i.startswith("__"))
    print(globals())
    a.append(x)
    return a


print(my_function(10))
# print(my_function(20, []))
# print(my_function(30))
# print(my_function(40))
# print(my_function(50))
