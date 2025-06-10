# paramaterized recurision :---> sum  of 1 to n number
# def Sum(sum, i, n):
#     if i > n:
#         print(f"sum of 1 to {n} numbers : {sum}")
#         return
#     Sum(sum + i, i + 1, n)


# Sum(0, 1, 10)


# functional recurision :--> it is works on return values
def output(n):
    if n == 1:
        return 1
    return n + output(n - 1)


print(output(10))

"""
def output(i,n):
    if i>n:
        return 0
    return i + output(i+1,n)

print(output(1,10))
"""
