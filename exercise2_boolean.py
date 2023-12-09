# task 1
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

# task 2 - move zeros to the end of the list
input_numbers = input("Please enter a few numbers, use coma symbol as separator: ")
list_of_numbers = input_numbers.split(",")

for number in list_of_numbers:
    if number == "0":
        list_of_numbers.remove(number)
        list_of_numbers.append(number)

print(list_of_numbers)

