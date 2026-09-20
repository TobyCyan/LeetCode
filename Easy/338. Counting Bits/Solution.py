class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        last_pow_of_2 = 2

        for i in range(min(n + 1, 2)):
            dp[i] = i

        def is_power_of_2(n):
            return n > 0 and (n & (n - 1)) == 0

        for i in range(2, n + 1):
            if is_power_of_2(i):
                last_pow_of_2 = i
                dp[i] = 1
            else:
                dp[i] = 1 + dp[i - last_pow_of_2]
        
        return dp