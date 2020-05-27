# Petq e gtnel 1-ic minejv n tveri faktorialneri gumar@.

# 5! = 1 * 2 * 3 * 4 * 5

# 4! = 1! * 2! * 3! * 4!  33
# 1! = 1  res = 1
# 2! = 1 * 2   res = 2
# 3! = 1 * 2 * 3   res = 6
# 4! = 1 * 2 * 3 * 4  res = 24

a = 4

result = 0

for i in range(1, a + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    result += factorial

print(result)


