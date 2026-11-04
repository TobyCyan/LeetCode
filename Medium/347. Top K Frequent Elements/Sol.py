from collections import Counter

import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqMap = Counter(nums)
        heap = []
        for num, freq in freqMap.items():
            heapq.heappush(heap, (-freq, num))
        
        result = []
        for _ in range(k):
            _, top = heapq.heappop(heap)
            result.append(top)
        
        return result
