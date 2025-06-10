# parameter tail recurion :--->
# print 1 to n number
# def Output(n):
#     if n == 0:
#         return
#     Output(n - 1)
#     print(n)


# Output(4)


# print n to 1 number
def result(n, i):
    if n == 0:
        return
    result(n - 1, i + 1)
    print(i)


result(4, 1)
