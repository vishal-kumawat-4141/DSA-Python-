# find the longest substring length without repeating characters :--->
# T.C = O(N ** 2) , S.C = O(N)
# class Solution:
#     def answer(self, s):
#         n = len(s)
#         long = 0
#         if n == 1:
#             return 1
#         for i in range(0, n - 1):
#             result = dict()
#             count = 1
#             result[s[i]] = 1
#             for j in range(i + 1, n):
#                 if s[j] not in result:
#                     result[s[j]] = 1
#                     count += 1
#                 else:
#                     break
#             if count >= long:
#                 long = count
#         return long


# s1 = Solution()
# print(s1.answer("vinit"))

# method 2:----->
# T.C = O(N ** 2) , S.C = O(N)
# class Solution:
#     def answer(self, s):
#         n = len(s)
#         maxi = 0
#         for i in range(0, n):
#             my_set = set()
#             for j in range(i, n):
#                 if s[j] in my_set:
#                     break
#                 maxi = max(maxi, j - i + 1)
#                 my_set.add(s[j])
#         return maxi


# s1 = Solution()
# print(s1.answer(""))


# method 3:--->
# T.C = O(N) , S.C = O(k) k is longest items
class Solution:
    def answer(self, s):
        n = len(s)
        maxi = 0
        left, right = 0, 0
        my_dict = dict()
        while right < n:
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)
            maxi = max(maxi, (right - left + 1))
            my_dict[s[right]] = right
            right += 1
        return maxi


s1 = Solution()
print(s1.answer(" "))
