# Longest Consecutive Sequence ....
# Method 1:--->
# nums = [102, 1, 99, 101, 98, 2, 5, 3, 99, 100]
# nums.sort()
# maxx = 0
# for i in range(0, len(nums)):
#     c = 0
#     p = 0
#     for j in range(0, len(nums)):
#         if nums[j] == nums[i] + p:
#             p += 1
#             c += 1
#     if maxx < c:
#         maxx = max(maxx, c)
# print(maxx
# Method 2:--->T.C = O(n^2) ,S.C = O(1)
# nums = [102, 1, 99, 101, 98, 2, 5, 3, 99, 100]
# maxx = 0
# for i in range(0, len(nums)):
#     count = 1
#     num = nums[i]
#     while num + 1 in nums:
#         count += 1
#         num += 1
#     if maxx < count:
#         maxx = max(maxx, count)
# print(maxx)


# Method 2:--->T.C = O(n^2) ,S.C = O(1)
# nums = [102, 1, 99, 101, 98, 2, 5, 3, 99, 100]
# nums.sort()
# print(nums)
# l_s = float("-inf")
# count = 0
# largest = 0
# for i in range(0, len(nums)):
#     num = nums[i]
#     if num - 1 == l_s:
#         count += 1
#         l_s = num
#     elif num != l_s:
#         count = 1
#         l_s = num
#     largest = max(largest, count)
# print(largest)

# Method 4:-->T.C = O(n) ,S.C = O(n)
nums = [102, 1, 99, 101, 98, 2, 5, 3, 99, 100]


def longest_squence(nums):
    my_set = set()
    for i in range(0, len(nums)):
        my_set.add(nums[i])
    largest = 0
    for num in my_set:
        if num - 1 not in my_set:  # O(1)
            x = num
            count = 1
            while x + 1 in my_set:  # t.c = O(1)
                count += 1
                x += 1
            largest = max(largest, count)
    return largest


print(longest_squence(nums))
