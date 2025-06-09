# print the divisiors which divide number ......

# Method 1 :---->
# n = int(input("Enter the number : "))
# result = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         result.append(i)
# print(f"{n} divide  number : {result}")

# T.C = O(n)  , S.C = O(k) k is number of divisiors

# Method 2 :----->
# n = int(input("Enter the number : "))
# result = []
# for i in range(1, (n // 2) + 1):
#     if n % i == 0:
#         result.append(i)
# result.append(n)
# print(f"{n} divide numbers : {result}")

# T.C = O(N/2) ~~O(N)   , S.C = O(k) k is number of divisiors

# Method 3:----->
from math import sqrt

n = int(input("Enter the number : "))
result = []
for i in range(1, int(sqrt(n) + 1)):
    if n % i == 0:
        result.append(i)
        if n / i not in result:
            result.append(int(n / i))

print(result)

# T.C = O(sqrt(n)) ,S.C = O(k)
