# convert the infix to pretfix expresstion:---->
# T.C = O(N)   , S.C = O(N) + O(N)


class Solution:
    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0

    def infix_to_prefix(self, s):
        s = s[::-1]  # O(N)
        s = s.replace("(", "temp").replace(")", "(").replace("temp", ")")  # O(N)
        stack = []
        result = []
        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()

            else:
                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result[::-1])  # O(N)


s1 = Solution()
print(s1.infix_to_prefix("(a+b)*c-d+f"))
