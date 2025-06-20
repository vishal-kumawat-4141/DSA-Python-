# Search in Rotated Sorted Array:----> if element present then return True else False
# Method 2 : --> T.C = O(log2(n)) , S.C = O(1)
# nums = [17, 18, 20, 1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16]


# def result(nums, target):
#     for i in range(0, len(nums)):
#         if nums[i] == target:
#             return True
#     return False


# print(result(nums, target=5))


# Method 2 : --> T.C = O(log2(n)) , S.C = O(1)
def search_ele(nums, target):
    n = len(nums)
    high = n - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False


nums = [17, 18, 20, 1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16]
print(search_ele(nums, target=101))
