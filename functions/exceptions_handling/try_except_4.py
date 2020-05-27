def my_function(dictionary):
    try:
        x = dictionary["number"]
        print(x + 5)
    except KeyError:
        print("KeyError")
        dictionary["number"] = 15
    except TypeError:
        print("TypeError")
        dictionary["number"] = int(dictionary["number"])
    except Exception as e:
        print("Another exception:", e)


my_dict = {"number": "15"}

my_function(my_dict)
print(my_dict)
