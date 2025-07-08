# print the list of next greater element form given array with forword and backword both side check greater :--->
class Solution:
    def greater(self, l):
        n = len(l)
        result = [-1] * n
        stack = []
        for i in range(((2 * n) - 1), -1, -1):
            while len(stack) != 0 and stack[-1] <= l[(i % n)]:
                stack.pop()
            if i < n:
                if len(stack) != 0:
                    result[i] = stack[-1]
            stack.append(l[i % n])
        return result


s1 = Solution()
print(s1.greater([2, 10, 12, 1, 11]))


num1 = [4, 1, 2]
num2 = [1, 3, 4, 2]
