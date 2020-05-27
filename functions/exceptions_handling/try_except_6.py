def my_function(x, y):
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
    except TypeError:
        x, y = int(x), int(y)

    print(x + y)


my_function("10", "20")
