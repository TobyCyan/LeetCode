class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        def score(i, j, k):
            return values[i] * values[j] * values[k]

        n = len(values)
        if n == 3:
            return score(0, 1, 2)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        def sub(i, j, k):
            return dp[i][k] + dp[k][j] + score(i, j, k)

        # Solve from smaller intervals
        for interval in range(3, n + 1):
            for i in range(n - interval + 1):
                j = i + interval - 1
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], sub(i, j, k))

        return dp[0][n - 1]
