class Solution:
    def numSquares(self, n: int) -> int:
        def is_perfect_square(x):
            sqr = int(x ** 0.5)
            return sqr * sqr == x

        dp = [0] * (n + 1)
        seen_ps = []

        # O(k) where k is # of perfect squares <= n
        def getMin(x):
            minValue = 10001
            for ps in seen_ps:
                minValue = min(minValue, dp[ps] + dp[x - ps])
            return minValue
        
        # O(n) x O(k) = O(nk)
        for i in range(1, n + 1):
            if is_perfect_square(i):
                dp[i] = 1
                seen_ps.append(i)
                continue

            dp[i] = getMin(i)
        return dp[n]
