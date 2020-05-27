# LEGB
# L => Local
# E => Enclosing
# G => Global
# B => Built-in

a = 30


def first_function():
    b = 15

    def second_function():
        c = 20

        def third_function():
            nonlocal c
            c += 1
            print(c)

        third_function()

    second_function()


first_function()
print(a)
