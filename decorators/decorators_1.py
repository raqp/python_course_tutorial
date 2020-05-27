def first_function(func):
    def second_functions():
        print("Code before func.")
        func()
        print("Code after func.")

    return second_functions


def some_decorator():
    print("I am a decorator.")


first_function(some_decorator)