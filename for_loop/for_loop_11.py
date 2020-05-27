#  5! = 1 * 2 * 3 * 4* 5 = 120

num = int(input("Enter your number: "))

a = 1

for i in range(1, num + 1):
    a *= i

print(a)
