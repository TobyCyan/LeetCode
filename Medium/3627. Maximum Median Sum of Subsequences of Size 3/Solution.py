from typing import List

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        groups = n // 3
        total = 0
        while groups > 0:
            total += nums[n - 2 * groups]
            groups -= 1
        
        return total