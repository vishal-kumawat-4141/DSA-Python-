# first and last occurnece of target value
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
        ub = -1
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
        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        ub = self.binary_ub(nums, target)
        if ub == -1:
            ub = len(nums)
        return [lb, ub - 1]


s1 = Solution()
print(s1.Result([3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15, 15], 8))
