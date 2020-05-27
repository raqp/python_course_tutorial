def my_func(*args, **kwargs):
    print(args)
    print(kwargs)


my_dict = {"x": 2, "y": 5, "z": 1, "t": 3}

my_func(1, 2, 34, x=25, y=15, b="hello")
