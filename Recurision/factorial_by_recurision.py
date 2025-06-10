# find the factorial of a number by recurison
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


num = int(input("Enter the positive  number : "))
print(f" {num} factoral is : ", fact(num))
