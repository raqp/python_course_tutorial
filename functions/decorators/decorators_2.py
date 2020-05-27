def login(some_function):
    def check_login_password(user, paswd):
        print("Start checking...")
        username, password = some_function()
        if user == username and password == paswd:
            print("Login success.")
        else:
            print("Login failed.")
        print("End checking...")

    return check_login_password


@login
def my_function():
    return "abc", 1525


my_function("acb", 1525)

my_function()
