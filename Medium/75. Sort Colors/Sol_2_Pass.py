class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        freqArr = [0] * 3
        for i in range(n):
            freqArr[nums[i]] += 1
        
        i = 0
        while freqArr[0] > 0:
            nums[i] = 0
            freqArr[0] -= 1
            i += 1
        
        while freqArr[1] > 0:
            nums[i] = 1
            freqArr[1] -= 1
            i += 1
        
        while freqArr[2] > 0:
            nums[i] = 2
            freqArr[2] -= 1
            i += 1
        