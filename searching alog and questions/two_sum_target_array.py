# sum of two indexs = target then print indexs
# T.C = O(n^2)  , S.C = O(1)
# l = [1, 2, 3, 4, 5, 6, 7, 8]


# def target_sum(l):
#     n = len(l)
#     target = 10
#     for i in range(0, n - 1):
#         for j in range(i + 1, n):
#             if l[i] + l[j] == target:
#                 # print([i, j]) # for  all indexs
#                 return [i, j]


# print(target_sum(l))


# T.C = O(n)  , S.C = O(n)
l = [1, 2, 3, 4, 5, 6, 7, 8]


def target_sum(l):
    n = len(l)
    target = 13
    hash_map = {}
    for i in range(0, n):
        remaning = target - l[i]
        if remaning in hash_map:
            return [hash_map[remaning], i]
        else:
            hash_map[l[i]] = i


print(target_sum(l))
