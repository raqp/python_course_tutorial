# min() funkciayi custom realisacian
# min() arg is an empty sequence


# def get_min(*args):
#     if not args:
#         raise ValueError("get_min() arg is an empty sequence")
#     minimum = args[0]
#     for number in args:
#         if number < minimum:
#             minimum = number
#     return minimum
#
#
# print(get_min())

def my_func(a, b, *args):
    print(a)
    print(b)
    print(args)


my_func(1, 2, 3, 34, 5, 6, 7, "a", 10)
