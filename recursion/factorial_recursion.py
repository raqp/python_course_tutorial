# 5! = 1 * 2 * 3 * 4 * 5


def factorial(n):
    if n <= 1:
        return 1
    s = n * factorial(n - 1)
    print(s)
    return s


print(factorial(5))
