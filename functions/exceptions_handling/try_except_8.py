def my_function(x, y):
    try:
        return x + y
    except TypeError:
        print("Error")
    finally:
        return "Bye"


print(my_function(15, 25))
