# find number of character form m to n lists using hashing and dictonary
# n = "azahsfaacd"
# m = ["a", "h", "p", "c"]
# hash_ch = [0] * 26
# for cn in n:
#     ascii_val = ord(cn)
#     index = ascii_val - 97
#     hash_ch[index] += 1

# for cm in m:
#     ascii_val = ord(cm)
#     index = ascii_val - 97
#     print(f"{cm} is occur in n : {hash_ch[index]}")


# T.C = O(n+m) , S.C = O(1)


# using dictonary
n = "azahsfaacd"
m = ["a", "h", "p", "c", "A", 9, "#"]
hash_dic = dict()
for cn in n:
    if cn in hash_dic:
        hash_dic[cn] += 1
    else:
        hash_dic[cn] = 1
for cm in m:
    if cm in hash_dic:
        print(f"{cm} occur in n : {hash_dic[cm]}")
    else:
        print(f"{cm} occur in n : 0")

# T.C = O(n+m) , S.C = O(1)


# n = "azahsfaacd"
# m = ["a", "h", "p", "c", "A", 9]
# result = []
# for ch in m:
#     count = 0
#     for i in n:
#         result.append(i)
#         if ch == i:
#             count += 1
#     print(f"{ch} is occurs in n : {count}")
