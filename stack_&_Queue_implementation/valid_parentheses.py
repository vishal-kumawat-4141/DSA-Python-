# return true and false for parantheses
class Solution:
    def check_parantheses(self, s):
        self.items = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                self.items.append(i)
            else:
                if len(self.items) == 0:
                    return False
                e = self.items.pop()
                if (
                    e == "("
                    and i == ")"
                    or e == "["
                    and i == "]"
                    or e == "{"
                    and i == "}"
                ):
                    continue
                else:
                    return False

        return len(self.items) == 0


s1 = Solution()
print(s1.check_parantheses("()"))
