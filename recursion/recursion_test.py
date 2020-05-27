def fib(n):
    a = 1
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return a


print(fib(10))
