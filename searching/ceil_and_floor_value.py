# ceil is  :--> smallest element of array >=target
# floor is :--> largest element of array <=target
# T.C = O(log2(n)) , S,C =O(1   )
def binary_s(nums, target):
    low = 0
    high = len(nums) - 1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    return [floor, ceil]


print(binary_s(nums=[3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15], target=11))
