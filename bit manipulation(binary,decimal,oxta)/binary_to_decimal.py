# convet binary to decimal number :--->
# T.C = O(len),S.C =O(1)
# def binary_2_decimal(num: list) -> int:
#     result = 0
#     num.reverse()
#     print(num)
#     for i in range(0, len(num)):
#         result += num[i] * pow(2, i)
#     return result


# print(binary_2_decimal([1, 0, 0, 1]))

# on string :---> using for loop
# def binary_2_decimal(num: str) -> int:
#     result = 0
#     # num.reverse()
#     # print(num)
#     for i in range(0, len(num)):
#         result += int(num[-(i + 1)]) * (2**i)
#     return result

# print(binary_2_decimal("1001"))

# using while loop :-->

# def binary_2_decimal(num: str) -> int:
#     result = 0
#     i = 0
#     while i < len(num):
#         result += int(num[-(i + 1)]) * (2**i)
#         i += 1
#     return result


# mehtod 4:-->
def binary_2_decimal(num: str) -> int:
    result = 0
    power = 0
    i = len(num) - 1
    while i >= 0:
        result += int(num[i]) * (2**i)
        i -= 1
        power += 1
    return result


print(binary_2_decimal("1001"))
