# soulutions of matrix
# basic matrix create
l = [[1, 2, 4], [5, 7, 3], [8, 9, 6]]
rows = len(l)
columns = len(l[0])
for i in range(0, rows):
    for j in range(0, columns):
        print(l[i][j], end=" ")
    print()
