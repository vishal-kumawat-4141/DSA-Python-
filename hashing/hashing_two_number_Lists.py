# With hashing compair two list data and print their frequency in another list
# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 7]
# m = [10, 111, 1, 9, 5, 67, 2]
# hash_list = [0] * 11
# for i in n:
#     hash_list[i] += 1
# for j in m:
#     if j >= 1 and j <= 10:
#         print(f"{j} occurs in n : ", hash_list[j])
#     else:
#         print(f"{j} occurs in n : 0")

# T.C = O(n+m) , S.C = O(1)


# using dictonary
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 7]
m = [10, 111, 1, 9, 5, 67, 2]
new_dic = dict()
for i in n:
    #     if i in new_dic:
    #         new_dic[i] += 1
    #     else:
    #         new_dic[i] = 1
    new_dic[i] = new_dic.get(n[i], 0) + 1

for j in m:
    if j not in new_dic:
        print(f"{j} occurs in n : 0")
    else:
        print(f"{j} cccurs in n :", new_dic[j])


# T.C = O(n+m) , S.C = O(1)
