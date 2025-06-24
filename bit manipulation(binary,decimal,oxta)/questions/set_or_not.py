# check ith bit is set or not  :----> using left shift
num = 13
i = 2
if (num & (1 << i)) != 0:
    print("True")
else:
    print("False")

# check ith bit is set or not  :----> using right shift
num = 13
i = 4
if (1 & (num >> i)) != 0:
    print("True")
else:
    print("False")
