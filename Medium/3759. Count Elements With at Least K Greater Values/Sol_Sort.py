from typing import List

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
        
        nums.sort()
        target = len(nums) - k
        targetNum = nums[target]

        count = 0
        for num in nums:
            if num < targetNum:
                count += 1
        return count
 