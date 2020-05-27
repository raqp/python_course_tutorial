def my_function(new_list):
    i = 0
    while i < len(new_list):
        yield new_list[i]
        i += 1


a = my_function([1, 2, 3, 4])


