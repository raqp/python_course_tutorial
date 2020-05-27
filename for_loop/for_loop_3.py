fruits = ["banana", "apple", "cherry", "orange"]

length = len(fruits)  # 4

# for index in range(length):
#     if fruits[index][0] == "a" or fruits[index][0] == "o":
#         print(fruits[index])

for i in range(length):
    if fruits[i][0] == "a" or fruits[i][0] == "o":
        fruits[i] = fruits[i].upper()

print(fruits)
