# clear ith index :---> mean if ith position is 1 then convert it 0 else 0
num = 13
i = 1
new = num & ~((1) << i)
print(new)
