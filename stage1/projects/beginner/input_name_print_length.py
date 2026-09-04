# WAP to input the first name and print its length

strU = str(input("Enter your first name: "))
print(len(strU))

# Using Function

def plength(name):
    return len(str(name))

print(plength(input("Enter your name: ")))
