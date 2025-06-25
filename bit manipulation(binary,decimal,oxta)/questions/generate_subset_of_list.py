# find the total subset of  given list:--->
# T.C  = O(2^n * n) ,S.C =  O(2^n * n)
nums = [1, 2, 3]
n = len(nums)
result = []
total_subset = 2**n  # 1<<n
for number in range(0, total_subset):
    list = []
    for i in range(0, n):
        if number & (1 << i) != 0:
            list.append(nums[i])
    result.append(list)
print(result)


# This is for understanding
# list = []
# for i in range(0, n):
#     if nums[0] & (1 << i) != 0:
#         list.append(nums[i])
# print(list)
