def first_function():
    a = 15

    def second_function():
        nonlocal a
        a += 1
        print(a)

        def third_function():
            print("hello")

        return third_function

    return second_function


print(first_function()()())
