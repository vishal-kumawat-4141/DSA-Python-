# make upper right tringle :---> * * *     _ * *      _ _ *
l = [[1, 2, 4], [5, 7, 3], [8, 9, 6]]
rows = len(l)
columns = len(l[0])
for i in range(0, rows):
    for j in range(0, columns):
        if j >= i:
            print(l[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()


# output:--->

# 1 2 4
#   7 3
#     6
