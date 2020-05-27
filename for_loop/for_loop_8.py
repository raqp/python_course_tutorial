fruits = ["banana", "apple", "cherry", "orange"]


for index, item in enumerate(fruits):
    if item[0] == "a" or item[0] == "o":
        fruits[index] = fruits[index].capitalize()

print(fruits)
# for index in range(len(fruits)):
#     print(index, fruits[index])
