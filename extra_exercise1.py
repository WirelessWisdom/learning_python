# task 1 -print all elements <5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(f'{i}\n')


# task 2 - return a list with matching elements
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
matching_list = []
for i in range(len(a)):
    if a[i] in b:
        matching_list.append(a[i])
print(matching_list)

# task 3 - sort a dictionary asc and desc
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
import operator
reversed_sorted_dict = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_dict)
print(reversed_sorted_dict)

# task 4 - unite dictionaries into one
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
new_dict = {**dict_a, **dict_b, **dict_c}
print(new_dict)

# task 5 - find 3 keys with the highest value
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)
print(result)

# task 10 - make a list and a tuple out of user input
user_input = input("Please enter some numbers: ").split(",")
some_list = []
some_tuple = ()
for i in user_input:
    some_list.append(int(i))

some_tuple = tuple(some_list)
print(some_list)
print(some_tuple)

#task 11 - print first and last element of the list
lst = [1, 2, 3, 4, 5]
print(f'First element: {lst[0]}\n Last element: {lst[-1]}')

