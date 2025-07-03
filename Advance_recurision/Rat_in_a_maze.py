# find the posibilities of rat in a maze:----->
# T.C = O(4 ** (m*n)) m = row and n = col , S.C = O(M * n) stack
class Solution:
    def findpath(self, i, j, maze, vis, move, result, n):
        if i == n - 1 and j == n - 1:
            result.append(move)
            return
        # down :--->
        if i + 1 < n and vis[i + 1][j] == 0 and maze[i + 1][j] == 1:
            vis[i][j] = 1
            self.findpath(i + 1, j, maze, vis, move + "D", result, n)
            vis[i][j] = 0

        # left :--->
        if j - 1 >= 0 and vis[i][j - 1] == 0 and maze[i][j - 1] == 1:
            vis[i][j] = 1
            self.findpath(i, j - 1, maze, vis, move + "L", result, n)
            vis[i][j] = 0

        # Right:---->
        if j + 1 < n and vis[i][j + 1] == 0 and maze[i][j + 1] == 1:
            vis[i][j] = 1
            self.findpath(i, j + 1, maze, vis, move + "R", result, n)
            vis[i][j] = 0

        # upper:---->
        if i - 1 >= 0 and vis[i - 1][j] == 0 and maze[i - 1][j] == 1:
            vis[i][j] = 1
            self.findpath(i - 1, j, maze, vis, move + "U", result, n)
            vis[i][j] = 0

    def Solve(self):
        matrix = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]]
        n = len(matrix)
        result = []
        vis = [[0 for _ in range(n)] for _ in range(n)]
        if matrix[0][0] == 1:
            self.findpath(0, 0, matrix, vis, "", result, n)
        return result


s1 = Solution()
print(s1.Solve())
