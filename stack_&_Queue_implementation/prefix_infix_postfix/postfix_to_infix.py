# convert the postfix to infix :--->
# T.C = O(N) , S.C = O(N)
class Solution:
    def postfix_to_Infix(self, s):
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                new_stack = f"({operand1}{char}{operand2})"
                stack.append(new_stack)
        return stack[-1]


s1 = Solution()
print(s1.postfix_to_Infix("abcd^e-*+"))
