from functools import cache

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)

        @cache
        def dp(c, remainingAmt):
            if c >= n or remainingAmt < 0:
                return float('inf')
            
            if remainingAmt == 0:
                return 0
            
            use = 1 + dp(c, remainingAmt - coins[c])
            notUse = dp(c + 1, remainingAmt)
            return min(use, notUse)
        
        result = dp(0, amount)
        if result == float('inf'):
            return -1
        return result