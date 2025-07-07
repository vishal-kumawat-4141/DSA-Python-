# convert the postfix to infix :---> this is start form last and the char between first pop and second pop element
# T.C = O(N) , S.C = O(N)
class Solution:
    def prefix_to_Infix(self, s):
        stack = []
        for char in s[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_stack = f"({operand1}{char}{operand2})"
                stack.append(new_stack)
        return stack[-1]


s1 = Solution()
print(s1.prefix_to_Infixfix("*+PQ-MN"))
