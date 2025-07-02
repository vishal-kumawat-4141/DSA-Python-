# combination sum III :---->
# T.C  =   O(2**9 ∗ K) ,S.C = O(n) stack space
class Solution:
    def combination(self, index, nums, subset, result, target, total):
        global k
        if index >= len(nums):
            if len(subset) == k and total == target:
                result.append(subset.copy())
            return
        if total > target or len(subset) > k:
            return
        subset.append(nums[index])
        summ = total + nums[index]
        self.combination(index + 1, nums, subset, result, target, summ)
        subset.pop()
        summ = total
        self.combination(index + 1, nums, subset, result, target, summ)
        return result


s1 = Solution()
k = 3
print(s1.combination(0, [1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], 9, 0))


# method 2:--># T.C  =   O(2**9 ∗ K) ,S.C = O(n) stack space
class Solution:
    def combination(self, last, nums, subset, result, target, total):
        global k
        if len(subset) == k and total == target:
            result.append(subset.copy())
            return
        if total > target or len(subset) > k:
            return
        for i in range(last, 10):
            summ = total + i
            subset.append(i)
            self.combination(i + 1, nums, subset, result, target, summ)
            subset.pop()
            summ = total
        return result


s1 = Solution()
k = 3
print(s1.combination(1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], 9, 0))
