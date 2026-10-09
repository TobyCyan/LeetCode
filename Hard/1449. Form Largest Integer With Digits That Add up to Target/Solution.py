from functools import cache

class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        n = len(cost)

        @cache
        def dp(i, c):
            if c == 0:
                return ''
            
            if i > n or c < 0:
                return None
            
            sub = dp(1, c - cost[i - 1])
            take = (str(i) + sub) if sub is not None else None
            noTake = dp(i + 1, c)

            if not take:
                return noTake
            if not noTake:
                return take

            return max(take, noTake, key=lambda s: (len(s), s))
        
        sol = dp(1, target)
        return '0' if not sol else sol