# def my_function(x, y):
#     return x + y

a = lambda x, y=10: x + y if x > y else x * y

print(a(5))
