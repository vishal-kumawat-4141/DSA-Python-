# remove duplicates form sorted array
# method -1 :--->
# l = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
# result = []


# def r_d(l, result):
#     for i in l:
#         if i not in result:
#             result.append(i)
#     return result


# print(r_d(l, result))

# method -2 :--->
# l = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
# new = set(l)
# result = list(new)
# print(result)

# method -3 :----> T.C = O(n*n) ,S.C = O(1)
# l = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]


# def duplicates(l):
#     for i in range(0, len(l) - 1):
#         if l[i] == l[i + 1]:
#             del l[i + 1]
#             return duplicates(l)
#     return l


# print(duplicates(l))
# duplicates(l)
# print(len(l))


# method -4:---->T.C = O(n) ,S.C = O(1)
# l = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
# n = len(l)


# def duplicates(l, n):
#     if n == 1:
#         return 1
#     i = 0
#     j = i + 1
#     while j < n:
#         if l[j] != l[i]:
#             i += 1
#             l[i], l[j] = l[j], l[i]
#         j += 1
#     return i + 1


# print(duplicates(l, n))


# method -5:----> T.C = O(n+n) ~~ O(n) ,S.C = O(n)
l = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
n = len(l)
result = {}


def duplicate(l, n, result):
    for i in range(0, n):
        result[l[i]] = 0
    j = 0
    for k in result:
        l[j] = k
        j += 1
    return j


print(duplicate(l, n, result))
