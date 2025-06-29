# find the combination sum without duplicates:---->
# T.C = O(2**n * k)  , S.C = O(n)
# class Solution:
#     def combination(self, index, nums, subset, total, ans, target):
#         if target == total:
#             if subset not in ans:
#                 ans.append(subset.copy())
#                 return
#         if total > target:
#             return
#         if index >= len(nums):
#             return
#         subset.append(nums[index])
#         s = total + nums[index]
#         self.combination(index + 1, nums, subset, s, ans, target)
#         s = total
#         subset.pop()
#         self.combination(index + 1, nums, subset, s, ans, target)

#     def add(self, nums, target):
#         nums.sort()
#         subset = []
#         ans = []
#         self.combination(0, nums, subset, 0, ans, target)
#         return ans


# s1 = Solution()
# print(s1.add([2, 5, 2, 1, 2], 5))


class Solution:
    def combination(self, index, nums, total, subset, result):
        if total == 0:
            result.append(subset.copy())
            return
        if total < 0:
            return
        if index >= len(nums):
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            summ = total - nums[i]
            self.combination(i + 1, nums, summ, subset, result)
            subset.pop()
        return result


s1 = Solution()
nums = [2, 5, 2, 1, 2]
nums.sort()
print(s1.combination(0, nums, 5, [], []))
