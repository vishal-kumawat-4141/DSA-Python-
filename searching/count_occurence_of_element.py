# count the occurence of element from sorted array
# Method 1.:---># T.C = O(n) , O(1)
# nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10, 10, 10]
# n = len(nums)
# first = -1
# last = -1


# def count_ele(nums, first, last, target):
#     for i in range(0, n):
#         if nums[i] == target:
#             if first == -1:
#                 first = i
#             last = i
#     if first == -1:
#         return 0
#     return last - first + 1


# print(count_ele(nums, first, last, target=10))


# Method 2.:---># T.C = O(log2(n)) , O(1)
class Solution(object):
    def binary_lb(self, nums, target):
        low = 0
        high = len(nums) - 1
        lb = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def binary_ub(self, nums, target):
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

    def Result(self, nums, target):
        lb = self.binary_lb(nums, target)
        if lb == -1:
            return 0
        ub = self.binary_ub(nums, target)
        return ub - lb


s1 = Solution()
print(s1.Result([3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15, 15], 12))

# Method 3.:---># T.C = O(log2(n)) , O(1)
# def result(nums, target):
#     n = len(nums)
#     low = 0
#     high = n - 1
#     lb = -1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] >= target:
#             lb = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     if lb == -1:
#         return 0
#     else:
#         n = len(nums)
#         ub = n
#         low = 0
#         high = n - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] > target:
#                 ub = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return ub - lb


# print(result(nums=[1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10, 10, 10], target=3))
