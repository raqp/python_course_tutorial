a = 15

my_list_1 = []
my_list_2 = []
my_list_3 = []

if a % 3 == 0:
    my_list_1.append(a)
    if a % 5 == 0:
        my_list_3.append(a)

if a % 5 == 0:
    my_list_2.append(a)

print(my_list_1)
print(my_list_2)
print(my_list_3)
