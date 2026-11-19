class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        total = 0
        m, n = len(worker), len(profit)
        
        def findHighestProfit(i):
            highest = 0
            for j in range(n):
                if worker[i] >= difficulty[j]:
                    highest = max(highest, profit[j])
            return highest

        # O(mn)
        for i in range(m):
            total += findHighestProfit(i)
        return total