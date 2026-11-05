class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def countingSort(nums, exp):
            n = len(nums)
            freq = [0] * 10

            for num in nums:
                idx = (num // exp) % 10
                freq[idx] += 1
            
            # Cumulative freq
            for i in range(1, 10):
                freq[i] += freq[i - 1]
            
            result = [0] * n
            for i in range(n - 1, -1, -1):
                idx = (nums[i] // exp) % 10
                result[freq[idx] - 1] = nums[i]

                freq[idx] -= 1
            
            nums[:] = result
        
        def radixSort(nums):
            if len(nums) == 0:
                return nums
            
            maxN = max(nums)
            exp = 1
            while maxN >= exp:
                countingSort(nums, exp)
                exp *= 10
            
            return nums
        
        negatives = []
        positives = []

        for num in nums:
            if num >= 0:
                positives.append(num)
            else:
                negatives.append(-num)

        sortedNg = radixSort(negatives)
        sortedPs = radixSort(positives)

        sortedNg = [-i for i in sortedNg[::-1]]

        return sortedNg + sortedPs