my_list_1 = ['a', 1, 'hi', 'Yerevan', {"one": 1}, 'flowers', 22, {"hello": "John"}, 55]

numbers_list = []
strings_list = []
dicts_list = []

for item in my_list_1:
    # if type(item) == dict:
    if isinstance(item, dict):
        dicts_list.append(item)
    elif isinstance(item, str):
        strings_list.append(item)
    elif isinstance(item, int):
        numbers_list.append(item)
    # else:
    #     numbers_list.append(item)


print(dicts_list)
