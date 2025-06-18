# 4 suum problems :--->
# T.C = O(n^3) == O(n^2) ,S.C = O(k) ,k is number of list output
# arr = [1, 0, -1, 0, -2, 2, 5, 9]
# n = len(arr)
# s = set()
# for i in range(0, n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             for l in range(k + 1, n):
#                 if arr[i] + arr[j] + arr[k] + arr[l] == 0:
#                     temp = [arr[i], arr[j], arr[k], arr[l]]
#                     temp.sort()
#                     s.add(tuple(temp))
# result = [list(ans) for ans in s]
# print(result)


# T.C =  O(n^2) ,S.C = O(n)+O(k) ,k is number of list output
# arr = [1, 0, -1, 0, -2, 2, 5, 9]
# n = len(arr)
# s = set()
# for i in range(0, n):
#     for j in range(i + 1, n):
#         my_set = set()
#         for k in range(j + 1, n):
#             forth = -(arr[i] + arr[j] + arr[k])
#             if forth in my_set:
#                 temp = [arr[i], arr[j], arr[k], forth]
#                 temp.sort()
#                 s.add(tuple(temp))
#             my_set.add(arr[k])
# result = [list(ans) for ans in s]
# print(result)


nums = [1, 0, -1, 0, -2, 2, 5, 9]
n = len(nums)
nums.sort()
result = []
for i in range(0, n):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    for j in range(i + 1, n):
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        l = j + 1
        k = n - 1
        while l < k:
            total = nums[i] + nums[j] + nums[l] + nums[k]
            if total < 0:
                l += 1
            elif total > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[l], nums[k]]
                result.append(temp)
                l += 1
                k -= 1
                while l < k and nums[l] == nums[l - 1]:
                    l += 1
                while l < k and nums[k] == nums[k + 1]:
                    k -= 1
print(result)
