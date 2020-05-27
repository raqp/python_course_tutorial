# Petq e hashvel my_list-i mej qani hat "h" tar ka
my_list = ["hello", "hi", "John", "hyperlink", "horse", "hopar"]

counter = 0

for word in my_list:
    for letter in word:
        if letter == "h":
            counter += 1


print(counter)

