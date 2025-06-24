# if ith bit is set then no change if ith bit is 0 then change 1
num = 13
i = 1
new = num | (1 << i)
print(new)
