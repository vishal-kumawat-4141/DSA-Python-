# Build an Array With Stack Operations :--> target start from 1 and target not == []
# method 2:--->
# T.C = O(N) , S.C = O(N)
class Solution:
    def buildArray(self, target, n):
        result = []
        s = [i for i in range(1, n + 1)]
        i = 0
        for j in range(target[-1]):
            if s[j] == target[i]:
                result.append("Push")
                if i < len(target):
                    i += 1
            else:
                result.append("Push")
                result.append("Pop")
        return result


s1 = Solution()
target = [1, 2, 4]
print(s1.buildArray(target, 5))


# method 2:--->
# T.C = O(N) , S.C = O(target[-1]) / O(1)  stack space
class Solution:
    def buildArray(self, target):
        result = []
        i = 0
        for j in range(target[-1]):
            if j + 1 == target[i]:
                result.append("Push")
                if i < len(target):
                    i += 1
            else:
                result.append("Push")
                result.append("Pop")
        return result


s1 = Solution()
target = [1, 2, 4]
print(s1.buildArray(target))
