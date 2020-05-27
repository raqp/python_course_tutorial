def custom_function(x, y, z, t, r):
    return x + y + z + t + r


my_list = [2, 5, 1, 7, 9]
print(custom_function(*my_list))
# my_dict = {"x": 2, "y": 5, "z": 1, "t": 3}


# def custom_function(x, y):
#     return x ** y
#
#
# for i in range(6):
#     result = custom_function(2, i)
#     print("Two to the power of", i, "equals:", result)
