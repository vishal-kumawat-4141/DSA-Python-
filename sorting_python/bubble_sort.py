# bubble sort :--> Accending order
num = [4, 5, 7, 2, 3, 1, 8, 9, 6]


def bubble_sort(num):
    for i in range(len(num) - 2, -1, -1):
        for j in range(0, i + 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return f"The sorting of bubble sort in accending order : {num}"


print(bubble_sort(num))

# bubble sort :--> decending order

num = [4, 5, 7, 2, 3, 1, 8, 9, 6]


def bubble_sort(num):
    for i in range(len(num) - 2, -1, -1):
        for j in range(0, i + 1):
            if num[j] < num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return f"The sorting of bubble sort in decending order : {num}"


print(bubble_sort(num))
