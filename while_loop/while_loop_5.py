from time import sleep

x = 0

while True:
    with open("new_file.txt", "a") as f:
        f.write(f"{x}\n")
    x += 1

    if x == 500:
        break
