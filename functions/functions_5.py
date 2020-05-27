# Function with default argument.

#
# def say_hi(name, message="Good evening"):
#     print(message, name, 10)
#
#
# say_hi("John", message="Good morning")
# say_hi("Robert")


def is_admin(name, admin=False):
    print(name, ", Is admin:", admin)


is_admin("John", True)
