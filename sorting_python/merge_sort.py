# merge sort :-----> it works on divide and conqure/ merge form ....


# left = [1, 2, 3, 4, 5]
# right = [2, 5, 7, 9, 10, 15, 16]
def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1

    return result


# dividing formate
arr = [10, 3, 5, 7, 2, 9, 1, 5, 15, 4, 2, 16]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left, right)


print(merge_sort(arr))
