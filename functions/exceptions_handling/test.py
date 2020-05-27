class MyCustomError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Another Error"

    def __str__(self):
        return self.message


def my_function():
    raise MyCustomError


my_function()
