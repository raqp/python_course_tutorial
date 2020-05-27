x = int(input("Enter your number: "))
y = int(input("Enter your number: "))

if x > y:
    x, y = y, x

for i in range(x, y + 1):
    print(i)
