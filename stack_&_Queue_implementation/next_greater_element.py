# print the list next greater element :--->
# T.C = O(N(N+1)/2) ~~ O(N ** 2) , S.C = O(N)
class Solution:
    def greater(self, l):
        result = [-1] * len(l)
        for i in range(0, len(l)):
            for j in range(i + 1, len(l)):
                if l[j] > l[i]:
                    result[i] = l[j]
                    break
        return result


s1 = Solution()
print(s1.greater([1, 3, 11, 10, 2, 4]))


# Method 2 :--> using montonic stack :---->
#  T.C = O(2N) , S.C = O(N)
class Solution:
    def greater(self, l):
        result = [-1] * len(l)
        s = []
        for i in range(len(l) - 1, -1, -1):
            while len(s) != 0 and s[-1] <= l[i]:
                s.pop()

            if len(s) == 0:
                s.append(l[i])

            elif s[-1] > l[i]:
                result[i] = s[-1]
                s.append(l[i])
        return result


s1 = Solution()
print(s1.greater([1, 3, 11, 10, 2, 4]))
print(s1.greater([19, 4, 2, 11, 6, 5, 3, 10]))


# method 3 :--->
#  T.C = O(2N) , S.C = O(N)
class Solution:
    def greater(self, l):
        result = [-1] * len(l)
        s = []
        for i in range(len(l) - 1, -1, -1):
            while len(s) != 0 and s[-1] <= l[i]:
                s.pop()

            if len(s) != 0:
                result[i] = s[-1]
            s.append(l[i])
        return result


s1 = Solution()
print(s1.greater([1, 3, 11, 10, 2, 4]))
print(s1.greater([19, 4, 2, 11, 6, 5, 3, 10]))
