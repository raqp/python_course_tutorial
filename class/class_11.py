def my_function(a, b):
    return a + b


foo = type("Foo", (), {"name": "John", "age": 10, "my_function": my_function})

print(foo.name)
print(foo.age)
foo.city = "Yerevan"
print(foo.my_function(10, 15))
