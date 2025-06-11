# Insertion sort:---> accending order
num = [3, 4, 5, 6, 8, 9, 10, 7, 1]


def insertion_sort(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and num[j] > key:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
    return f"The sorting with insertion sort in accending order : {num}"


print(insertion_sort(num))

# Insertion sort:---> decending order
num = [3, 4, 5, 6, 8, 9, 10, 7, 1]


def insertion_sort(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and num[j] < key:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
    return f"The sorting with insertion sort in decending order : {num}"


print(insertion_sort(num))
