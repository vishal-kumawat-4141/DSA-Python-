# convert prefix to postfix :--->
# T.C = O(N) , S.C = O(N)
class Solution:
    def prefix_to_postfix(self, s):
        stack = []
        for char in s[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_stack = f"{operand1}{operand2}{char}"
                stack.append(new_stack)
        return stack[-1]


s1 = Solution()
print(s1.prefix_to_postfix("*+PQ-MN"))
print(s1.prefix_to_postfix("/-AB*+DEF"))
