# find the maximum subarray of sum ..
# Method 2 :---->T.C = O(n^2) , S.C = O(1)

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max = float("-inf")
# for i in range(0, len(nums)):
#     summ = 0
#     for j in range(i, len(nums)):
#         summ += nums[j]

#         if max < summ:
#             max = summ
# print(max)


# Method 2 :---->T.C = O(n) , S.C = O(1)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxx = float("-inf")

summ = 0
for i in range(0, len(nums)):
    summ += nums[i]
    maxx = max(maxx, summ)
    if summ < 0:
        summ = 0

print(maxx)
