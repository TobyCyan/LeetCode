class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            rob = nums[i] + dp[i - 2]
            noRob = dp[i - 1]
            dp[i] = max(rob, noRob)
        
        return dp[n - 1]
