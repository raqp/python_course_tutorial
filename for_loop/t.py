my_string = "one two"
x = ""

for index, item in enumerate(my_string):
    if item == " ":
        x = my_string[index + 1:] + " " + my_string[:index]
        break

print(x)
