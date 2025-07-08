# find next greater element I :---->
# T.C = O(N) , S.C = O(N)


class Solution:
    def greater(self, num1, num2):
        result = [-1] * len(num2)
        s = []
        ans = []
        d = dict()
        for i in range(len(num2) - 1, -1, -1):
            while len(s) != 0 and s[-1] <= num2[i]:
                s.pop()

            if len(s) != 0:
                result[i] = s[-1]
            s.append(num2[i])
        for i in range(len(result)):
            d[num2[i]] = result[i]
        for i in range(len(num1)):
            ans.append(d[num1[i]])
        return ans


s1 = Solution()
num1 = [4, 1, 2]
num2 = [1, 3, 4, 2]
print(s1.greater(num1, num2))
