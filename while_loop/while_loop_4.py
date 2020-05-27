a = ["a", "b", "c", "d", "e"]
i = 0

while i < len(a):
    if a[i] == "d":
        i += 1
        continue
    print(a[i])
    i += 1
