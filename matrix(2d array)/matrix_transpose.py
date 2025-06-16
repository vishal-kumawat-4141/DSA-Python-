# print diagonal (left to right )
l = [[1, 2, 4], [5, 7, 3]]
rows = len(l)
columns = len(l[0])
Transpose = [[0] * rows for i in range(0, columns)]
for i in range(0, rows):
    for j in range(0, columns):
        Transpose[j][i] = l[i][j]

print(Transpose)

# result = [[l[j][i] for j in range(0, rows)] for i in range(0, columns)]
# print(result)
