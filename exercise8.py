# task1 - group_by_surname
# group names: "A-I", "J-P", "Q-T", "U-Z"
import string

list_of_characters = ["John Snow", "Aegon Targarien", "Jamie Lannister", "Eddard Stark", "Robert Baratheon",
                      "Jorah Mormont", "Theon Greyjoy", "Khal Drogo", "Grey Worm"]


def group_by_surname(list_of_enrollees):
    group_A_I_counter = 0
    group_J_P_counter = 0
    group_Q_T_counter = 0
    group_U_Z_counter = 0
    for name in list_of_enrollees:
        surname = name.split(" ")[1]
        if surname[0] in group_A_I:
            group_A_I_counter += 1
        elif surname[0] in group_J_P:
            group_J_P_counter += 1
        elif surname[0] in group_Q_T:
            group_Q_T_counter += 1
        elif surname[0] in group_U_Z:
            group_U_Z_counter += 1
    print(f"The number of students in groups:\n"
          f"A-I: {group_A_I_counter}\n"
          f"J-P: {group_J_P_counter}\n"
          f"Q-T: {group_Q_T_counter}\n"
          f"U-Z: {group_U_Z_counter}\n")
    return None


group_A_I = string.ascii_letters[string.ascii_letters.index("A"):string.ascii_letters.index("I") + 1]
group_J_P = string.ascii_letters[string.ascii_letters.index("J"):string.ascii_letters.index("P") + 1]
group_Q_T = string.ascii_letters[string.ascii_letters.index("Q"):string.ascii_letters.index("T") + 1]
group_U_Z = string.ascii_letters[string.ascii_letters.index("U"):string.ascii_letters.index("Z") + 1]

group_by_surname(list_of_characters)


# task 2 - first word in a string
def first_word(user_input):
    word = ""
    for char in user_input:
        if char.isalpha() or char == "'":
            word += char
        else:
            if word:
                return word.strip("!,.+-=/")
    return word.strip("!,.+-=/")


sentence = input("Please enter a string: ")
print(first_word(sentence))


# task 3 - return list of elemnts from iterables

def lchain(*args, **kwargs):
    new_list = []
    for arg in args:
        for i in arg:
            new_list.append(i)
    return new_list


assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]


# task 4

def some_gen(begin, n, func):
    i = 0
    while i <= n:
        result = func(begin)
        yield result
        i += 1
        begin = result

def pow(x):
    return x**2


print(list(some_gen(2, 4, pow)))