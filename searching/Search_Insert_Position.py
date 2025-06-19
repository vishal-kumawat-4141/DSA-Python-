# search insert element  form list :----->
# method 2:----> linear search
# def binary_s(nums, target):
#     low = 0
#     high = len(nums) - 1
#     lb = len(nums)
#     if nums[0] > target:
#         lb = 0
#     elif nums[-1] < target:
#         lb = len(nums)
#     for i in range(0, len(nums) - 1):
#         if nums[i] < target:
#             if nums[i + 1] > target:
#                 lb = i + 1
#     return lb


# print(binary_s(nums=[1, 1, 1, 2, 2, 2, 4, 4, 6, 7], target=100))


# method 2:-->
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


print(binary_s(nums=[1, 1, 1, 2, 2, 2, 4, 4, 5, 5, 6], target=3))
