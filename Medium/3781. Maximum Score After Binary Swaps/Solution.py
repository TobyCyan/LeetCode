from typing import List
import heapq

class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        n = len(nums)
        heap = []
        total = 0
        for i in range(n):
            heapq.heappush_max(heap, nums[i])
            if s[i] == '1':
                total += heapq.heappop_max(heap)

        return total
