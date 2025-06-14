# find maximum consecutive ones in array

# Method 1:---> T.C = O(n) , S.C = O(1)
# l = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# max = 0
# c = 0
# for i in range(0, len(l)):
#     if l[i] == 1:
#         c += 1
#         if max < c:
#             max = c
#     else:
#         c = 0

# print(f"maximum count of 1 occurs in array :", max)

# method 2 :----> T.C = O(n) , S.C = O(1)
l = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
maxi = 0
c = 0
for i in range(0, len(l)):
    if l[i] == 1:
        c += 1

    else:
        max_value = max(maxi, c)
        c = 0
print(f"maximum count of 1 occurs in array :", max(max_value, c))
