class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        for i in range(1, n):
            sub = float('inf')
            for k in range(i):
                if k + nums[k] >= i:
                    sub = min(sub, 1 + dp[k])
            dp[i] = sub
        return dp[n - 1]
