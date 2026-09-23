from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def cost(i, j):
            return costs[j - 1] + (j - i) ** 2
        
        # Defined as minimum total cost to reach step n from step i
        minC = [0] * (n + 1)
        minC[n] = 0
        minC[n - 1] = cost(n - 1, n)

        def sub(i, j):
            if j > n:
                # Impossible to reach.
                return float('inf')
            
            return cost(i, j) + minC[j]
        
        for i in range(n - 2, -1, -1):
            minC[i] = min(sub(i, i + 1), sub(i, i + 2), sub(i, i + 3))

        return minC[0]
