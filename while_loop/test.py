# 1, 1, 2, 3, 5, 8 , 13, 21, 34, 55...


i = int(input())
a = 1
b = 1
start = time()
for j in range(2, i):
    a, b = b, a + b


