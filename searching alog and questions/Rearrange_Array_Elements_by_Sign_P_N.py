# rearrange array elements by positive then negative elements
# Method 1:---->
# T.C = O(2n)~~~O(n)  , S.C = O(n)
# nums = [3, 1, -2, -5, 2, -4]
# p_l = []
# n_l = []
# result = []
# n = len(nums)
# for i in range(0, n):
#     if nums[i] < 0:
#         n_l.append(nums[i])
#     else:
#         p_l.append(nums[i])

# for j in range(0, n // 2):
#     result.append(p_l[j])
#     result.append(n_l[j])

# print(result)

# Method 2:-->
# T.C = O(2n)~~~O(n)  , S.C = O(n)
# nums = [3, 1, -2, -5, 2, -4]
# p_l = []
# n_l = []
# n = len(nums)
# for i in range(0, n):
#     if nums[i] < 0:
#         n_l.append(nums[i])
#     else:
#         p_l.append(nums[i])

# for j in range(0, len(p_l)):
#     nums[2 * j] = p_l[j]
#     nums[(2 * j) + 1] = n_l[j]

# print(nums)


# Method 3:-->
# T.C = O(n)  , S.C = O(n)
nums = [3, 1, -2, -5, 2, -4]
result = [0] * len(nums)
p = 0
n = 1
for i in range(0, len(nums)):
    if nums[i] > 0:
        result[p] = nums[i]
        p += 2
    else:
        result[n] = nums[i]
        n += 2
print(result)
