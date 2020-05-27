template_1 = "{food}, {city}, {number}"
template_1 = template_1.format(food="barbecue", city="Yerevan", number=15)
template_2 = "Hello +++++++ {}".format(template_1)
template_3 = "{0} ==== {1}".format(template_1, template_2)

# custom_dict = {"one": 1, "two": 2, "three": 3}

# template = "{one} === {two} === {three}".format(**custom_dict)
# print(template)

# t = ("three", 3)
