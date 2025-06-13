# move zeros in end of list ...

# Method 1:----->
# l = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]


# def Result(l):
#     for i in range(0, len(l) - 1):
#         if l[i] == 0 and l[i + 1] != 0:
#             l[i], l[i + 1] = l[i + 1], l[i]
#             return Result(l)
#     return l


# print(Result(l))

# Method 2:----->
# l = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]


# def result(l):
#     for i in range(0, len(l) - 1):
#         if l[i] == 0 and l[i + 1] != 0:
#             e = l.pop(i)
#             l.append(e)
#             return result(l)

#     return l


# print(result(l))

# Method 3 -----> T.C = O(n+n) ~~ O(n)  , S.C = O(n)
# l = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
# temp = []
# for i in range(0, len(l)):
#     if l[i] != 0:
#         temp.append(l[i])

# n2 = len(temp)
# for j in range(0, n2):
#     l[j] = temp[j]

# for k in range(n2, len(l)):
#     l[k] = 0

# print(l)


# Method 4. -----> T.C = O(n)  , S.C = O(1)
l = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]


def result(l):
    if len(l) == 0:
        return
    i = 0
    while i < len(l):
        if l[i] == 0:
            break
        i += 1
        if i == len(l):
            return
        j = i + 1

    while j < len(l):
        if l[j] != 0:
            l[i], l[j] = l[j], l[i]
            i += 1
        j += 1
    return l


print(result(l))
