sorted_list = [9, 3, 2, 8, 6, 7]


def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    for j in range(n):
        for i in range(n - 1 - j):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
    return list_to_sort


print(bubble_sort(sorted_list))
