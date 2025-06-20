# search in rotated array :---> minimum element
# Method 1:---> T.C = O(n) , S.C = (1)
# nums = [4, 5, 6, 7, 0, 1, 2]
# min = float("inf")
# for i in range(0, len(nums)):
#     if nums[i] <= min:
#         min = nums[i]
# print(min)


# Method 2:---> T.C = O(log2(n)) ,S.C = O(1)
def search_ele(nums):
    n = len(nums)
    high = n - 1
    low = 0
    m = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= nums[high]:
            m = min(m, nums[mid])
            high = mid - 1
        else:
            m = min(m, nums[mid])
            low = mid + 1
    return m


nums = [4, 5, 6, 7, -2, -1, 0, 1, 2]
print(search_ele(nums))
