def first_function(some_function):
    def second_function():
        print("Before some_function.")
        some_function()
        print("After some_function.")

    return second_function


@first_function
def my_function():
    print("This is my_function.")


my_function()
