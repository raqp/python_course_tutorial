# Petq e gtnel amen elementic qani hat ka trvac listi mej

d = {4: 2}

my_list = [4, 9, 4, 13, 9, 13, 10, 10, 13, 7, 9, 13, 12, 9, 4, 5, 9, 12, 11, 6, 8, 5, 6, 13, 5, 8, 6, 6, 8, 4]

# print(not bool(d.get("a")))

for i in my_list:
    if not d.get(i):
        d[i] = 1
    else:
        d[i] = d[i] + 1

# print(d)
