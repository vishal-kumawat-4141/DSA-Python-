# right rotation by 1 place in array
# method 1 :---> using slicing
l = [1, 2, 3, 4, 5, 6, 7]
n = len(l)
l[:] = [l[n - 1]] + l[0 : n - 1]  # l[:] use for same list l address
print(l)


# method 2 --> using for loop
# l = [1, 2, 3, 4, 5, 6, 7]
# n = len(l)
# temp = l[n - 1]
# for i in range(n - 2, -1, -1):
#     l[i + 1] = l[i]
# l[0] = temp
# print(l)
