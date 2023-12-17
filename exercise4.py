# task 1 - unification of values on the list of dictionaries
from collections import defaultdict
data_example = [{"item": "item1", "amount": 400}, {"item": "item2", "amount": 300}, {"item": "item1", "amount": 750}]

result = defaultdict(int)
for i in data_example:
    result[i['item']] += int(i['amount'])
print(result)


# task 2 - count the number of inputted symbols
result = {}
user_input = input("Please enter something: ")
for i in user_input:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)


# task 3 - create a dictionary to group a sequence of tuples
original_list = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
ordered_dictionary = {}
for i in range(0, len(original_list)):
    key = original_list[i][0]
    if key not in ordered_dictionary:
        ordered_dictionary[key] = [original_list[i][1]]
    else:
        ordered_dictionary[key].append(original_list[i][1])
print(ordered_dictionary)


# task 4 - find a pair of elements, which sum is equal to a defined value
first_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
first_expected_value = 35
elements_of_first_sum = ()
first_list_of_tuples = []
for first in range(0, len(first_list)):
    for second in range(0, len(first_list)):
        if first_list[first] + first_list[second] == first_expected_value and first != second:
            elements_of_first_sum = (first_list[first], first_list[second])
            first_list_of_tuples.append(elements_of_first_sum)
print(first_list_of_tuples)


second_list = [1, 2, 3, 4, 5]
second_expected_value = 5
elements_of_second_sum = ()
second_list_of_tuples = []
for first_first in range(0, len(second_list)):
    for second_second in range(0, len(second_list)):
        if second_list[first_first] + second_list[second_second] == second_expected_value and first_first != second_second:
            elements_of_second_sum = (second_list[first_first], second_list[second_second])
            second_list_of_tuples.append(elements_of_second_sum)
print(second_list_of_tuples)