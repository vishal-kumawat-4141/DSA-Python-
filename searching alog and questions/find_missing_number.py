# find missing number from array ..
# using for loop :--->T.C = O(n^2)  , S.C = O(1)
# l = [1, 2, 0, 4]
# for i in range(0, len(l)+1):
#     if i not in l:
#         print(i)


# using while loop :----> T.C = O(n^2)  , S.C = O(1)
# l = [1, 2, 0, 4]
# i = 0
# while i < len(l) + 1:
#     if i not in l:
#         print(i)
#     i += 1


# using dictonary :---> T.C = O(n+n+n) ~~~ O(n)  , S.C = O(n)
# l = [1, 2, 0, 4]
# result = dict()


# def missing_ele(l, result):
#     for i in range(0, len(l) + 1):
#         result[i] = 0

#     for j in l:
#         result[j] = 1

#     for k, v in result.items():
#         if v == 0:
#             return k


# print(missing_ele(l, result))


# using sum  :---> T.C = O(n)  , S.C = O(1)
# l = [1, 2, 0, 4]
# sum = 0
# total = 0
# for i in range(0, len(l)):
#     sum = sum + l[i]
#     total += i + 1
# if sum == total:
#     print(f"All elements found in list .")
# else:
#     print(f"missing element is : {total-sum}")


# another some method: --> T.C = O(n)  , S.C = O(1)
l = [1, 2, 0, 4]


def missing_ele(l):
    n = len(l)
    return (n * (n + 1) // 2) - sum(l)


print(missing_ele(l))
