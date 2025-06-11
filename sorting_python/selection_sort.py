# selection sorting :---> In accending order
# num = [5, 3, 6, 4, 9, 1, 10, 2]


# def selsection(num):
#     for i in range(0, len(num)):
#         min_index = i
#         for j in range(i + 1, len(num)):
#             if num[min_index] > num[j]:
#                 min_index = j
#         num[i], num[min_index] = num[min_index], num[i]
#     return f"The sorted array is : {num}"


# print(selsection(num))


# selection sorting :---> In decending order
num = [5, 3, 6, 4, 9, 1, 10, 2]


def selsection(num):
    for i in range(0, len(num)):
        max_index = i
        for j in range(i + 1, len(num)):
            if num[max_index] < num[j]:
                max_index = j
        num[i], num[max_index] = num[max_index], num[i]
    return f"The sorted array is : {num}"


print(selsection(num))
