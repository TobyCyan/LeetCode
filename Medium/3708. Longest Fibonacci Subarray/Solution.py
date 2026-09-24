from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = 2
        longest = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[i - 1] + nums[i - 2]:
                curr = 2
                continue
            curr += 1
            longest = max(curr, longest)
        return longest