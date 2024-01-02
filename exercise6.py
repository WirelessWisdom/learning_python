# task 1 - roman numbers

def roman_to_integer(roman_number, *args):
    numbers_correspondence = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    final_number = 0
    i = 0
    while i < len(roman_number) - 1:
        if numbers_correspondence[roman_number[i]] < numbers_correspondence[roman_number[i + 1]]:
            final_number += numbers_correspondence[roman_number[i + 1]] - numbers_correspondence[roman_number[i]]
            i += 2
        else:
            final_number += numbers_correspondence[roman_number[i]]
            i += 1
    if i == len(roman_number) - 1:
        final_number += numbers_correspondence[roman_number[i]]
    return final_number


user_number = input("Please enter a roman number: ")
print(roman_to_integer(user_number))


# task 2 - add_one

def add_one(list_of_numbers):
    added_one = list_of_numbers[-1]
    new_value = int(added_one) + 1
    if new_value < 10:
        list_of_numbers[-1] = new_value
    else:
        holder = 1
        for i in range(len(list_of_numbers) - 1, -1, -1):
            current_sum = list_of_numbers[i] + holder
            list_of_numbers[i] = current_sum % 10
            carry = current_sum // 10

        if holder:
            list_of_numbers.insert(0, holder)

    return list_of_numbers


first_group_of_numbers = [1, 2, 3, 4]
# second_group_of_numbers = [9, 9, 9, 9]
second_group_of_numbers = [8, 8, 9]
print(add_one(first_group_of_numbers))
print(add_one(second_group_of_numbers))


# task 3 - is_palindrome

def is_palindrome(input_sentence):
    fixed_sentence = ''.join(char.lower() for char in input_sentence if char.isalnum())
    return fixed_sentence == fixed_sentence[::-1]


sentence1 = "A man, a plan, a canal, Panama!"
print(is_palindrome(sentence1))
sentence2 = "Hey, bitch"
print(is_palindrome(sentence2))
