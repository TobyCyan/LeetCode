from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return n

        curr, max_len = 1, 1
        for i in range(1, n, 1):
            if nums[i] > nums[i - 1]:
                curr += 1
                max_len = max(curr, max_len)
            else:
                curr = 1
        
        return max_len
        