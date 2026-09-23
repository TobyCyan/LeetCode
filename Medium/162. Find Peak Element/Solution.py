class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        def valid(idx):
            return idx >= 0 and idx < n

        def peak(idx):
            left = idx - 1
            right = idx + 1
            curr = nums[idx]
            return (not valid(left) or nums[left] < curr) and (not valid(right) or nums[right] < curr)

        def leftPeak(idx):
            left = idx - 1
            curr = nums[idx]
            return valid(left) and nums[left] > curr

        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if peak(mid):
                return mid
            
            if leftPeak(mid):
                r = mid - 1
            else:
                l = mid + 1
        