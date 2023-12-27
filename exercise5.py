# task 1 - say-hi function

def say_hi(name, age, *args):
    print(f"Hi. My name is {name} and I'm {age} years old")


name_input = input("Please enter your name: ")
age_input = input("Please enter your age: ")
say_hi(name_input, age_input)


# task 2 - correct sentence
def correct_sentence(sentence, *args):
    sentence = sentence.capitalize()
    last_char = sentence[-1]
    if last_char == ".":
        print(sentence)
    else:
        print(sentence + ".")


sentence_to_correct = input("Please enter your sentence: ")
correct_sentence(sentence_to_correct)

# task 3 - second_index
string_input = input("Please enter your string: ")
symbol_input = input("Please enter a symbol: ")


def second_occurrence_symbol_search(string, symbol, *args):

    list_of_symbol = []
    for i in range(len(string)):
        if string[i] == symbol:
            list_of_symbol.append(symbol)
            if len(list_of_symbol) > 1:
                return i
    return None

# try to use approach with find/index to use couple of symbols in input
print(second_occurrence_symbol_search(string_input, symbol_input))

# task 4 - common_elements
import random
number_of_elements = int(input("Please enter number of elements: "))


def common_elements(number, *args):
    first_set = set()
    second_set = set()

    for i in range(0, number):
        while len(first_set) < number:
            a = random.randint(0, 99)
            if a % 3 == 0:
                first_set.add(a)
        while len(second_set) < number:
            b = random.randint(0, 99)
            if b % 5 == 0:
                second_set.add(b)


    print(first_set)
    print(second_set)

    intersection = first_set.intersection(second_set)
    print(intersection)


common_elements(number_of_elements)
