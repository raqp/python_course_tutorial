b = [1, 2, 3, 4, 5]

# for num in a:
#     print(num)

a = iter(b)
k = next(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(a)
print(b)
print(k)
