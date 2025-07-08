# return the result of asteroid colision form given array :------>
# T.C = O(2N) ~~ O(N)  , S.C =O(K) K is stack space
class Solution:
    def asteroid(self, nums):
        n = len(nums)
        s = []
        for i in range(n):
            if nums[i] > 0:
                s.append(nums[i])
            else:
                while len(s) != 0 and abs(nums[i]) > s[-1] and s[-1] > 0:
                    s.pop()
                if len(s) != 0 and abs(nums[i]) == s[-1]:
                    s.pop()
                elif len(s) == 0 or s[-1] < 0:
                    s.append(nums[i])
        return s


s1 = Solution()
print(s1.asteroid([7, 1, 1, 2, -3, -7, 17, 15, -18, -19]))
