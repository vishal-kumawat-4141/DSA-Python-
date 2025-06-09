# find the frequency map in form dictonary ....
# method 1 :----->
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 6, 5]
# result = {}
# for i in n:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
# print(f"frequency of numbers in dictonary is : {result}")

# T.C = O(n) , S.C = O(k)


# Method 2. :--->
# get method
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 6, 5]
result = {}
l = len(n)
for i in range(0, l):
    result[n[i]] = result.get(n[i], 0) + 1
print(result)

# T.C = O(n) , S.C = O(k)  k is number of keys
