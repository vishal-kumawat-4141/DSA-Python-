# Solve the N-Queen problem :---->
# method 1 :---> T.C = O(N! * N)  ,S.C = (N**2 +N) stack space
class Solution:

    def isSafe(self, row, col, board, n):
        duprow = row
        dupcol = col
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
            row -= 1
        row = duprow
        col = dupcol
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        return True

    def solve(self, col, board, n, result):
        if col == n:
            result.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                self.solve(col + 1, board, n, result)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
        return result


s1 = Solution()
n = 4
board = ["." * n for i in range(n)]
# board[0] = board[0][:0] + "Q" + board[0][0 + 1 :]
# print(board)
result = []
print(s1.solve(0, board, n, result))


# method 2:--->
# T.C = O(N!) , S.C = O(N **2)
class Solution:
    def solve(self, col, board, left_row, upper_diagonal, lower_diagonal, result, n):
        if col == n:
            result.append(list(board))
            return
        for row in range(n):
            if (
                left_row[row] == 0
                and upper_diagonal[(n - 1) + (col - row)] == 0
                and lower_diagonal[row + col] == 0
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                left_row[row] = 1
                upper_diagonal[(n - 1) + (col - row)] = 1
                lower_diagonal[row + col] = 1
                self.solve(
                    col + 1, board, left_row, upper_diagonal, lower_diagonal, result, n
                )
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                left_row[row] = 0
                upper_diagonal[(n - 1) + (col - row)] = 0
                lower_diagonal[row + col] = 0

    def Solve_N_Queen(self, n):
        result = []
        board = ["." * n for i in range(n)]
        left_row = [0] * n
        upper_dignal = [0] * ((2 * n) - 1)
        lower_dignal = [0] * ((2 * n) - 1)
        self.solve(0, board, left_row, upper_dignal, lower_dignal, result, n)
        return result


s1 = Solution()
print(s1.Solve_N_Queen(4))
