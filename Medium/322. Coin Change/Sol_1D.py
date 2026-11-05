from functools import cache

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)

        @cache
        def dp(amount):
            if amount < 0:
                return float('inf')
            
            if amount == 0:
                return 0
            
            best = float('inf')
            for coin in coins:
                best = min(best, 1 + dp(amount - coin))

            return best

        result = dp(amount)
        if result == float('inf'):
            return -1
        return result