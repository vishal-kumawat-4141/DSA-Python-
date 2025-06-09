# count the digit of given number ....

# Mehtod 1 :---->
# n = 6537
# digit = len(str(n))
# print(digit)

# T.c = O(1) ,S.c = O(1)


# Method 2 --->
# n = 6537
# num = n
# count = int(0)
# while num > 0:
#     digit = num % 10
#     count += 1
#     num = num // 10
# print(count)

# T.C = O(log10(N)) ,S.C(1)

# Method 3 :--->
from math import *

n = 6537
digit = int(log10(n) + 1)
print(digit)

# T.C = O(1) , S.C = O(1)
