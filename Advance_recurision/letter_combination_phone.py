# letter combination of 2 - 9 for phone :-->
# T.C = O(4 ** n * n) , S.C = O(k) k is stack space
class Solution:
    def phone(self, index, digits, result, subset, hash_map):
        if index >= len(digits):
            result.append("".join(subset))
            return
        for ch in hash_map[digits[index]]:
            subset.append(ch)
            self.phone(index + 1, digits, result, subset, hash_map)
            subset.pop()

        return result


s1 = Solution()
hash_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqus",
    "8": "tuv",
    "9": "wxyz",
}
print(s1.phone(0, "", [], [], hash_map))
