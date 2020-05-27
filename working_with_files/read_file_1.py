# File bacelu hamar ogtagordzvum e open() function@.
# Orinak

f = open("my_file.txt")
print(f.read())

# Ete noric pordzenq tpel f.read()-@ kstananq datark string.
f.seek(0)
print(f.read())

f.close()
