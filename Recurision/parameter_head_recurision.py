# parameter head recurisions :--->
# def output(i, n):
#     if n == 0:
#         return
#     print(i)
#     output(i, n - 1)


# output(20, 4)


# print 1 to n number using parameter head recurision
# def Print(i, n):
#     if i > n:
#         return
#     print(i)
#     Print(i + 1, n)


# Print(1, 4)


# print n to 1 number without i parameter
def result(n):
    if n == 0:
        return
    print(n)
    result(n - 1)


result(4)
