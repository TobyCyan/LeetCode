class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        d = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            canSegment = False
            for j in range(i):
                canSegment = canSegment or (dp[j] and s[j:i] in d)
                if canSegment:
                    dp[i] = canSegment
                    break

        return dp[n]