# 3sum problems :-->
# T.C = O(n^3) == O(n^2) ,S.C = O(k) ,k is number of list output
# arr = [-1, 0, 1, 2, -1, 4]
# n = len(arr)
# s = set()
# for i in range(0, n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if arr[i] + arr[j] + arr[k] == 0:
#                 temp = [arr[i], arr[j], arr[k]]
#                 temp.sort()
#                 s.add(tuple(temp))
# result = [list(ans) for ans in s]
# print(result)

# T.C =  O(n^2) ,S.C = O(n)+O(k) ,k is number of list output
# arr = [-1, 0, 1, 2, -1, 4]
# n = len(arr)
# s = set()
# for i in range(0, n):
#     my_set = set()
#     for j in range(i + 1, n):
#         third = -(arr[i] + arr[j])
#         if third in my_set:
#             temp = [arr[i], arr[j], third]
#             temp.sort()
#             s.add(tuple(temp))
#         my_set.add(arr[j])
# result = [list(ans) for ans in s]
# print(result)


# T.C =  O(nlogn)+O(n^2) ,S.C = O(k)/ O(1) ,k is number of list output
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
arr.sort()
result = []
for i in range(0, n):
    if i != 0 and arr[i] == arr[i - 1]:
        continue
    j = i + 1
    k = n - 1
    while j < k:
        total = arr[i] + arr[j] + arr[k]
        if total < 0:
            j += 1
        elif total > 0:
            k -= 1
        else:
            temp = [arr[i], arr[j], arr[k]]
            result.append(temp)
            j += 1
            k -= 1
            while j < k and arr[j] == arr[j - 1]:
                j += 1
            while j < k and arr[k] == arr[k + 1]:
                k -= 1
print(result)
