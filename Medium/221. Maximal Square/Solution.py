class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if matrix[0][0] == '1' else 0

        maxDp = dp[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if matrix[i][j] == '1':
                    dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j - 1], 1 + dp[i - 1][j - 1])
                    maxDp = max(maxDp, dp[i][j])

        return maxDp ** 2