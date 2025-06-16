# print diagonal (left to right )
l = [[1, 2, 4], [5, 7, 3], [8, 9, 6]]
rows = len(l)
columns = len(l[0])
for i in range(0, rows):
    for j in range(0, columns):
        if i == j:
            print(l[i][j], end=" ")
        else:
            print("", end=" ")
    print()

print()
# output:---->
# 1
#  7
#   6

# second diagonal (right to left )
l = [[1, 2, 4], [5, 7, 3], [8, 9, 6]]
rows = len(l)
columns = len(l[0])
for i in range(0, rows):
    for j in range(0, columns):
        if i + j == rows - 1:
            print(l[i][j], end=" ")
        else:
            print("", end=" ")
    print()

# output:--->
"""
  4
 7
8
"""
