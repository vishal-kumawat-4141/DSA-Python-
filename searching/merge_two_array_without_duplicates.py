# merge two array without duplicates
# l1 = [1, 2, 3, 4, 4, 5, 6, 7, 7]
# l2 = [2, 2, 2, 3, 4, 5, 5, 6, 6]

# new = []


# def result(l1, l2, new):
#     for i in l1:
#         if i not in new:
#             new.append(i)
#     for j in l2:
#         if j not in new:
#             new.append(j)
#     return new


# print(result(l1, l2, new))


# Method 2 :---->
l1 = [1, 2, 3, 4, 4, 5, 6, 7, 7]
l2 = [2, 2, 2, 3, 4, 5, 5, 6, 6]
new = []


def result(l1, l2, new):
    i, j = 0, 0
    n, m = len(l1), len(l2)
    while i < n and j < m:
        if l1[i] <= l2[j]:
            if len(new) == 0 or new[-1] != l1[i]:
                new.append(l1[i])
            i += 1
        else:
            if len(new) == 0 or new[-1] != l2[j]:
                new.append(l2[j])
            j += 1

    while i < n:
        if len(new) == 0 or l1[i] != new[-1]:
            new.append(l1[i])
        i += 1

    while j < m:
        if len(new) == 0 or new[-1] != l2[j]:
            new.append(l2[j])
        j += 1
    return new


print(result(l1, l2, new))
