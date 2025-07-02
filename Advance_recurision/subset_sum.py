# find the subset of sum :-->
# method 1:---> T.C = O(2 ** n) , S.C = O(n)  n is stack space
class Solution:
    def sub(self, index, nums, result, subset):
        if index >= len(nums):
            result.append(sum(subset.copy()))
            return
        subset.append(nums[index])
        self.sub(index + 1, nums, result, subset)
        subset.pop()
        self.sub(index + 1, nums, result, subset)
        # print(result)


s1 = Solution()
result = []
s1.sub(0, [1, 2, 3], result, [])
print(result)


# method 2:---> T.C = O(2 ** n) , S.C = O(n) . n is stack space
class Solution:
    def sub(self, index, nums, result, total):
        if index >= len(nums):
            result.append(total)
            return
        summ = total + nums[index]
        self.sub(index + 1, nums, result, summ)
        summ = total
        self.sub(index + 1, nums, result, summ)
        # print(result)


s1 = Solution()
result = []
s1.sub(0, [1, 2, 3], result, 0)
print(result)
