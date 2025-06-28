# find combindation of target sum :--->
# T.C = O(2**t * k)  ,S.C = O(t) t is stack space
class Solution:
    def combinations(self, index, total, subset, nums, result, target):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if index >= len(nums):
            return
        subset.append(nums[index])
        sum = total + nums[index]
        self.combinations(index, sum, subset, nums, result, target)
        # e = subset.pop()
        # sum = sum - e
        sum = total
        subset.pop()
        self.combinations(index + 1, sum, subset, nums, result, target)
        return result


s1 = Solution()
nums = [2, 3, 6, 7]
print(s1.combinations(0, 0, [], nums, [], 9))
