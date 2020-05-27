def my_function(x, y):
    try:
        print(x + y)
    except TypeError:
        print(5 / 0)
    finally:
        print(int(x) + int(y))


my_function(10, "25")
