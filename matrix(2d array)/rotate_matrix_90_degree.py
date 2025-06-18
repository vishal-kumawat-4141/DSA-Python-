# rotate matrix by 90 degree for n * n matrix
""" "
1   2   3   4                   13   9  5  1
5   6   7   8                   14   10 6  2
9  10  11  12          ---->    15   11 7  3
13 14  15  16                   16   12 8  4

"""

# Method 1:---> T.C = O(n^2) ,S.C = O(n^2)
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# row = len(matrix)
# column = len(matrix[0])
# result = [[0 for _ in range(0, row)] for _ in range(0, column)]
# for i in range(0, row):
#     for j in range(0, column):
#         result[j][(row - 1) - i] = matrix[i][j]

# print(result)

# method 2:--->T.C = O(n^2) ,S.C = O(n^2)
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# row = len(matrix)
# column = len(matrix[0])


# def rotation(matrix, row, column):
#     rotate_matrix = [
#         [matrix[j][i] for j in range(row - 1, -1, -1)] for i in range(0, column)
#     ]

#     for i in range(0, row):
#         for j in range(0, column):
#             matrix[i][j] = rotate_matrix[i][j]
#     return matrix


# print(rotation(matrix, row, column))


# method 3 :---> T.C = O(n^2)+ O(n^2) == O(n^2) ,S.C = O(1)
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
row = len(matrix)
column = len(matrix[0])
for i in range(0, row - 1):
    for j in range(i + 1, column):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(0, row):
    matrix[i].reverse()  # T.C = O(n)

print(matrix)
