# Nerdrvac funkcianeri hamar gordzum e lriv nuyn logikan: ete uzum enq global scopum haytararac popoxakani
# arjeq@ poxenq partadir petq e dimenq global operatori ognutyan@.
# Nshanakutyun chuni te vor nerdrvac funkciayi mej enq uzum poxenq global scope-um exac popoxakani arjeq@
# Bolor depqerum petq e ogtagordzenq global operator@

num = 15


def first_function():
    def second_function():
        global num
        num += 1
        print(num)
    second_function()


first_function()
print(num)
