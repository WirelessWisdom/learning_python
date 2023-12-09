age = int(input("Please enter your age: "))

if age < 2:
    print("You are a baby")
elif 2 <= age < 4:
    print("You are a kid")
elif 4 <= age < 13:
    print("You are a child")
elif 13 <= age < 20:
    print("You are a teenager")
elif 20 <= age < 65:
    print("You are a gown-up")
else:
    print("You are a senior")