

# for i in range(len(a)):
#     print(a)
#     a.pop()

a = ["a", "b", "c", "d", "e"]
#   [ 0,   1,   2,   3,   4 ]
#   [-5,  -4,  -3,  -2,  -1 ]

while a:
    print(a)
    # a = a[:-1]
    a.pop()
