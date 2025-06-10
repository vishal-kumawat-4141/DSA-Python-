# check string is palindrome or not
# s = input("Enter a string : ")


# def palindrome(l=0, r=len(s) - 1):
#     global s
#     if l >= r:
#         return "string is palindrome"
#     elif s[l] != s[r]:
#         return "string is not palindrome"
#     return palindrome(l + 1, r - 1)


# print(palindrome())

# T.C = O(n/2) ~~ O(n)
# S.C = O(n/2) ~~ O()  stack space


# using loop
def palidrome():
    s = input("enter the string :")
    n = len(s)
    l = 0
    r = n - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return "string is not palindrome"
    return "string is palindrome ."


print(palidrome())
