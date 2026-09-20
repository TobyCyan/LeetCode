from functools import cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        B, S = 0, 1

        @cache
        def dp(i, state):
            if i >= n:
                return 0

            if state == B:
                buy = dp(i + 1, S) - prices[i]
                cd = dp(i + 1, state)
                return max(buy, cd)
            else:
                sell = dp(i + 2, B) + prices[i]
                cd = dp(i + 1, state)
                return max(sell, cd)
        
        return dp(0, B)