# find the largest element from the array ...
# l = [1, 4, 55, 76, 94, 140, 37]
# largest = l[0]
# n = len(l)
# for i in range(0, n):
#     largest = max(largest, l[i])
# print(f"largest element from {l} is : {largest}")


# using infinity :-->
# l = [1, 4, 55, 76, 94, 140, 37]
# largest = float("-inf")
# n = len(l)
# for i in range(0, n):
#     largest = max(largest, l[i])
# print(f"largest element from {l} is : {largest}")


# using function :---->>>>
l = [1, 4, 55, 76, 94, 140, 37]


def largest_ele(l):
    largest = l[0]
    n = len(l)
    for i in range(0, n):
        largest = max(largest, l[i])
    return f"largest element is : {largest}"


print(largest_ele(l))
