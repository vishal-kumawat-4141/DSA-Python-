# lower bound :---> smallest index of nums[i] >= target value
# T.C = O(log2(n)) ,O(1)
def binary_s(nums, target):
    low = 0
    high = len(nums) - 1
    lb = len(nums)
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb


print(binary_s(nums=[1, 1, 1, 2, 2, 2, 4, 4, 5, 5, 6], target=1))


# upper bound :---> smallest index of nums[i] > target value
# T.C = O(log2(n)) ,O(1)
def binary_s(nums, target):
    low = 0
    high = len(nums) - 1
    ub = len(nums)
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub


print(binary_s(nums=[1, 1, 1, 2, 2, 2, 4, 4, 5, 5, 6], target=1))
