class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxS, minS = 0, 0
        ans = 0
        
        for n in nums:
            maxS = max(n + maxS, 0)
            minS = min(n + minS, 0)
            ans = max(ans, max(maxS, abs(minS)))
        
        return ans
    