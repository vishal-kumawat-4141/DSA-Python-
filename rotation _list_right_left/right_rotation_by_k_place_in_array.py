# right rotation by k places in array

# Method -1:--->
# l = [1, 2, 3, 4, 5, 6, 7]
# n = len(l)
# k = 3
# rotation = k % n
# l[:] = l[-rotation:] + l[: rotation + 1]
# print(l)


# # method -2
# l = [1, 2, 3, 4, 5, 6, 7]
# n = len(l)
# k = 3
# rotation = k % n
# for _ in range(0, rotation):
#     e = l.pop()
#     l.insert(0, e)
# print(l)


# mehtod - 3 :--->
l = [1, 2, 3, 4, 5, 6, 7]
n = len(l)


def reverse_arrary(l, left, right):
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1


k = 3
reverse_arrary(l, n - k, n - 1)
reverse_arrary(l, 0, n - k - 1)
reverse_arrary(l, 0, n - 1)
print(l)
