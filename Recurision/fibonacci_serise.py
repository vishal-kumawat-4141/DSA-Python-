# fibonacci serise
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


N = int(input("Enter the number : "))
print(fibonacci(N))
