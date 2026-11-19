class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        total = 0
        m, n = len(worker), len(profit)

        # Guarantee that if a worker can do a job,
        # they get the best profit for that difficulty out of all jobs with difficulties <= their capability
        jobs = sorted(zip(difficulty, profit))
        difficulties = []
        bestProfits = []
        best = 0
        for d, p in jobs:
            best = max(best, p)
            bestProfits.append(best)
            difficulties.append(d)
        
        def findHighestProfit(i):
            highest = 0
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                diff = difficulties[mid]
                if worker[i] >= diff:
                    highest = max(highest, bestProfits[mid])
                    l = mid + 1
                else:
                    r = mid - 1
                
            return highest
        
        for i in range(m):
            total += findHighestProfit(i)
        return total