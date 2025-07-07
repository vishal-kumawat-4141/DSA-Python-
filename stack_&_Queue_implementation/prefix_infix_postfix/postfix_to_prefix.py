# convert to postfix to prefix :---> char position is starting then last pop then first pop
# T.C = O(N) , S.C = O(N)
class Solution:
    def postfix_to_prefix(self, s):
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                new_stack = f"{char}{operand1}{operand2}"
                stack.append(new_stack)
        return stack[-1]


s1 = Solution()
print(s1.postfix_to_prefix("AB-DE+F*/"))
