def first_function():
    a = 15

    def second_function():
        nonlocal a
        a += 1
        print(a)

    return second_function


x = first_function()
x()
