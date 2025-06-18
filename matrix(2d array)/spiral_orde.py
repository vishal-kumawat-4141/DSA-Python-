# spiral order matrix => convert in a single list output
matrix = [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11],
]

row = len(matrix)
column = len(matrix[0])
top = 0
left = 0
right = column - 1
buttom = row - 1
l = []

while top <= buttom and left <= right:
    # for left to right move
    for i in range(left, right + 1):
        l.append(matrix[top][i])
    top += 1

    # for top to buttom move
    for i in range(top, buttom + 1):
        l.append(matrix[i][right])
    right -= 1

    # for right to left move
    if top <= buttom:
        for i in range(right, left - 1, -1):
            l.append(matrix[buttom][i])
        buttom -= 1

    # for buttom to top move
    if left <= right:
        for i in range(buttom, top - 1, -1):
            l.append(matrix[i][left])
        left += 1
print(l)
