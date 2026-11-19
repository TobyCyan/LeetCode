class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        n = len(profit)

        jobs = sorted(zip(difficulty, profit))

        worker.sort()

        # O(m + n)
        j, best, total = 0, 0, 0
        for w in worker:
            while j < n and jobs[j][0] <= w:
                best = max(best, jobs[j][1])
                j += 1
            total += best
        return total