while True:
    try:
        x = int(input("Enter some number: "))
        print(f"2 ** {x} = {2 ** x}")
    except ValueError:
        print("That was no valid number.  Try again...")
    print()


