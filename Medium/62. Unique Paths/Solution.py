class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Let dp[i][j] be the number of possible unique paths to reach grid[m - 1][n - 1] from grid[i][j]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]