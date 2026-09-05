n1 = int(input("Enter the 1st Number: "))
n2 = int(input("Enter the 2nd Number: "))
n3 = int(input("Enter the 3rd Number: "))

if n1 > n2:
    if n1 > n3:
        print(f"The greatest is: {n1}")
    else:
        print(f"The greatest is: {n3}")
else:
    if n2 > n3:
        print(f"The greatest is: {n2}")
    else:
        print(f"The greatest is: {n3}")
    