from typing import List

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        def partition(p, arr):
            n = len(arr)
            pivot = arr[p]
            l = 0
            r = n - 1
            arr[p], arr[r] = arr[r], arr[p]

            for i in range(n - 1):
                if arr[i] <= pivot:
                    arr[l], arr[i] = arr[i], arr[l]
                    l += 1
            
            arr[r], arr[l] = arr[l], arr[r]
            return l
        
        n = len(nums)
        result = 0
        # O(n^2)
        for i in range(n):
            rank = partition(i, nums.copy())
            count = n - rank - 1
            if count >= k:
                result += 1
        return result