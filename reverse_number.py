# print the reverse of a number

# Method 1:---->
# n = 1345
# num = n
# while num > 0:
#     digit = num % 10
#     print(digit, end="")
#     num = num // 10

# T.C = O(log10(n)) , S.C = O(1)

# method 2 ---->
n = 1345
num = n
result = 0
while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num = num // 10
print("Reverse number is :", result)

# T.C = O(log10(n)) , S.C = O(1)
