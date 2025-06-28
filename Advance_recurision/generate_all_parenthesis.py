# generate all parenthesis :----->>
# T.C = O(2**n) , S.C = O(k) k is stack space
class Solution:
    def para(self, index, total, nums, result):
        if index >= len(nums):
            if total == 0:
                result.append("".join(nums))
            return
        if total > len(nums) // 2 or total < 0:
            return
        nums[index] = "("
        self.para(index + 1, total + 1, nums, result)
        nums[index] = ")"
        self.para(index + 1, total - 1, nums, result)

    def Answer(self, n):
        nums = [""] * (2 * n)
        result = []
        self.para(0, 0, nums, result)
        return result


s1 = Solution()
print(s1.Answer(3))
