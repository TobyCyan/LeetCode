class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]