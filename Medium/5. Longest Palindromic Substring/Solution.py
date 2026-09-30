class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        bestI, bestJ = 0, 0
        for length in range(1, n + 1):
            for j in range(length - 1, n):
                i = j - length + 1

                if s[i] != s[j]:
                    continue

                if length <= 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j] and length > bestJ - bestI + 1:
                    bestI, bestJ = i, j

        return s[bestI : bestJ + 1]