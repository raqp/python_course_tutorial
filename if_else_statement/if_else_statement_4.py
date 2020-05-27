# my_list_1-i mej pahvum en ayn tver@ voronq aranc mnacord bajanvum en 3-i
# my_list_2-i mej pahvum en ayn  tver@ voronq aranc mnacord bajanvum en 5-i
# my_list_3-i mej pahvum en ayn  tver@ voronq aranc mnacord bajanvum en ev 3-i, ev 5-i.

a = 5

my_list_1 = []
my_list_2 = []
my_list_3 = []

if a % 3 == 0:
    my_list_1.append(a)

if a % 5 == 0:
    my_list_2.append(a)

if a % 3 == 0 and a % 5 == 0:
    my_list_3.append(a)

print(my_list_1)
print(my_list_2)
print(my_list_3)
