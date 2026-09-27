class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        ans = 0

        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            
            ans = max(ans, price - buy_price)
        
        return ans