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