class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag algorithm
        n = len(nums)
        l, m, r = 0, 0, n - 1
        while m <= r:
            mid = nums[m]
            if mid == 0:
                nums[l], nums[m] = nums[m], nums[l]
                m += 1
                l += 1
            elif mid == 1:
                m += 1
            else:
                # mid num is 2
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
        