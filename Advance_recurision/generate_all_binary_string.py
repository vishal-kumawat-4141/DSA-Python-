# generate all binary string :--->
class Solution:
    def backtrack(self, index, flag, number, result):
        if index >= len(number):
            result.append("".join(number))
            return
        number[index] = "0"
        self.backtrack(index + 1, True, number, result)
        if flag == True:
            number[index] = "1"
            self.backtrack(index + 1, False, number, result)
            number[index] = "0"

    def binary(self, n):
        number = ["0"] * n
        result = []
        self.backtrack(0, True, number, result)
        return result


s1 = Solution()
print(s1.binary(3))
