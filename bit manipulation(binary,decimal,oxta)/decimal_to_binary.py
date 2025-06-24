# conver number decimal to binary number :---->
# T.C =O(log2(n)) , S.C = O(log2(n))
def decimal_2_binary(num: int) -> str:
    result = ""
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2
    result = result[::-1]
    return result


print(decimal_2_binary(1))
