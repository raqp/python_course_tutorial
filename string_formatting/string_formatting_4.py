# Mi qani orinak % formatting-ic.

a = "Four float numbers example: %s --- %s --- %s --- %s" % (11.2, 15.9, 3.14, 25.0)

info = {"name_1": "Jimmy", "age_1": 14, "name_2": "Robert", "age_2": 20, "name_3": "Richard", "age_3": 10, "abc": {"one": 1}}


jimmy_info = "My name is %(name_1)s, I'm %(age_1)d years old." % info  # {"name_1": "Jimmy", "age_1": 14}
robert_info = "My name is %(name_2)s, I'm %(age_2)d years old." % info  # {"age_1": 14, "name_2": "Robert"}
richard_info = "My name is %(name_3)s, I'm %(age_3)d years old." % info  # {"name_3": "Richard", "age_3": 10}

print(jimmy_info)
print(robert_info)
print(richard_info)
