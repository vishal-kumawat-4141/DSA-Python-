# print lower right tingle
l = [[1, 2, 4], [5, 7, 3], [8, 9, 6]]
rows = len(l)
columns = len(l[0])
for i in range(0, rows):
    for j in range(0, columns):
        if i + j >= columns - 1:
            print(l[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
