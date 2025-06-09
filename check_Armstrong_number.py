# check number is armstrong number or not ....
n = int(input("Enter the number : "))
num = n
result = 0
digit = len(str(n))
while num > 0:
    d = num % 10
    result += d**digit
    # result += pow(d, digit)
    num //= 10
if result == n:
    print(f"{n} is a armstrong number .")
else:
    print(f"{n} is not a armstrong number .")

# T.C = O(log10(N)) , S.C = O(1)
