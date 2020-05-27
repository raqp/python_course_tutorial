# Xndri e arajanum erb vor funkciayi mej uzum enq popoxenq global tiruytum haytararvac popoxakan@
# Nman xndir@ lucelu hamar partadir petq e ogtagordzel global operator@, vorin kheteven global tiruytum
# grvac popoxakanner@

num = 20


def my_function():
    global num
    num += 1
    print(num)


my_function()
print(num)
num += 1
print(num)
my_function()
