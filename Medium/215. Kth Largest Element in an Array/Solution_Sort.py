import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # O((n + k)logn)
        heapq.heapify_max(nums)

        largest = 0
        for _ in range(k):
            largest = heapq.heappop_max(nums)
        
        return largest