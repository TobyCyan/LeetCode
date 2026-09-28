class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        ans, curr_goal, max_reach = 0, 0, 0
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == curr_goal:
                ans += 1
                curr_goal = max_reach
        return ans