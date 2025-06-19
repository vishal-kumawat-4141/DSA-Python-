# binary search ----> complexity is O(log2(n)) , mid,low,high

# Method 1 :---> using iterative form
# T.C = O(logn) , S.C = O(1)

# nums = [2, 4, 6, 7, 9, 11, 18, 19]
# target = 6
# def binary_s(nums, target):
#     low1 = 0
#     high1 = len(nums) - 1
#     while low1 <= high1:
#         mid = (low1 + high1) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high1 = mid - 1
#         elif nums[mid] < target:
#             low1 = mid + 1
#     return -1
# print(binary_s(nums=[2, 4, 6, 7, 9, 11, 18, 19], target=6))


# Method 2 :--> using recurision
# T.C = O(log2(n))) , S.C = O(1)
def binary_s(nums, target, low1, high1):
    if low1 <= high1:
        mid = (low1 + high1) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            # high1 = mid - 1
            return binary_s(nums, target, low1, high1=mid - 1)

        else:
            # low1 = mid + 1
            return binary_s(nums, target, high1=n - 1, low1=mid + 1)
    else:
        return -1


nums = [2, 4, 0, 7, 9, 11, 18, 19]
n = len(nums)
print(binary_s(nums=[2, 4, 6, 7, 9, 11, 18, 19], target=6, low1=0, high1=n - 1))
