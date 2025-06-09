# check number is palindrome or not

# Method. 1 :------>
n = 545
num = n
result = 0
while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num //= 10
if result == n:
    print(f"{n} is palindrome number .")
else:
    print(f"{n} is not palindrome number .")

# T.C = O(log10(n)) S.C = O(1)
