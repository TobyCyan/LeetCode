from linecache import cache

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        @cache
        def dp(i, robbedFirstDay):
            if i >= n or i == n - 1 and robbedFirstDay:
                return 0
            
            firstDay = i == 0
        
            if firstDay:
                rob = nums[i] + dp(i + 2, True)
                noRob = dp(i + 1, False)
                return max(rob, noRob)
            
            rob = nums[i] + dp(i + 2, robbedFirstDay)
            noRob = dp(i + 1, robbedFirstDay)
            return max(rob, noRob)

        return dp(0, False)
