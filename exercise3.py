# task1 - calculator
import string

while True:
    first_input_number = input("Please enter first number: ")
    if first_input_number == "quit":
        print("You successfully quited")
        break

    math_operator = input("Please enter math operator: ")
    if math_operator == "quit":
        print("You successfully quited")
        break

    second_input_number = input("Please enter second number: ")
    if second_input_number == "quit":
        print("You successfully quited")
        break

    first_number = int(first_input_number)
    second_number = int(second_input_number)

    if math_operator == "+":
        result = first_number + second_number
        print(result)
    elif math_operator == "-":
        result = first_number - second_number
        print(result)
    elif math_operator == "*":
        result = first_number * second_number
        print(result)
    elif math_operator == "/":
        if second_number == 0:
            print("Division by zero is forbidden")
            break
        else:
            result = first_number / second_number
            print(result)

# task 2 - divide a list by 2
new_list = []
first_list =[]
second_list =[]

new_list = input("Please enter a list: ").split(",")
number_of_symbols = len(new_list)

if number_of_symbols % 2 == 0:
    index = int(number_of_symbols / 2)
    i = 0
    for i in range(0, index):
        item = new_list[i]
        first_list.append(item)
        i = i + 1
    for i in range(index,number_of_symbols):
        item = new_list[i]
        second_list.append(item)
        i = i + 1
elif number_of_symbols % 2 > 0:
    index = int(number_of_symbols / 2) + 1
    i = 0
    for i in range(0, index):
        item = new_list[i]
        first_list.append(item)
        i = i + 1
    for i in range(index, number_of_symbols):
        item = new_list[i]
        second_list.append(item)
        i = i + 1
else:
    first_list = []
    second_list = []

final_list = [first_list, second_list]
print(final_list)

# task 3 - multiplication
user_number = input("Please enter your number: ")
list_of_numbers = []
multiplication_result = 1

if int(user_number) > 0:
    for n in user_number:
        list_of_numbers.append(int(n))

    for m in list_of_numbers:
        multiplication_result = multiplication_result * m
    print(multiplication_result)
else:
    print("Number should be > 0")

# task 4 - move 0 to the end of the list
user_list = list(input("Please enter list of numbers with zeros: ").split(","))
for number in user_list:
    if int(number) == 0:
        user_list.remove(number)
        user_list.append(number)
print(user_list)

# task 5 - random list
import random
number_of_elements_in_random_list = random.randrange(3,10)
list_randomized = []
for i in range(0,number_of_elements_in_random_list):
    list_randomized.append(random.randint(0,99))
print(f"Initial randomized list: {list_randomized}")
new_randomized_list = []
new_randomized_list.append(list_randomized[0])
new_randomized_list.append(list_randomized[2])

second_element_from_the_end = int(len(list_randomized)) - 2
new_randomized_list.append(list_randomized[second_element_from_the_end])
print(f"Final randomized list of 3 elements: {new_randomized_list}")

# task 6 - return all symbols between 2 symbols
user_symbols = input("Please enter two symbols in a format a-Z: ").split("-")
first_symbol = user_symbols[0]
second_symbol = user_symbols[1]

start_symbol = string.ascii_letters.index(first_symbol)
end_symbol = string.ascii_letters.index(second_symbol)

result_string = string.ascii_letters[start_symbol:end_symbol + 1]
print(result_string)