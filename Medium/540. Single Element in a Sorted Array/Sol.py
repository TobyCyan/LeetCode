from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        def inBounds(idx):
            return idx >= 0 and idx < n
        
        def isOdd(idx):
            return idx % 2 != 0

        while l <= r:
            mid = l + (r - l) // 2
            isLeftNeighbourMe = inBounds(mid - 1) and nums[mid - 1] == nums[mid]
            isRightNeighbourMe = inBounds(mid + 1) and nums[mid + 1] == nums[mid]
            if not isLeftNeighbourMe and not isRightNeighbourMe:
                return nums[mid]
            
            """
            Rationale:
            If the mid element is the Nth element where N is odd and it is the first of its pair,
            that means there are an even number of elements to the left which are properly paired.
            So the single element must be to the right.

            On the other hand, if the mid element is the second of its pair,
            that means there are an even number of elements to the left, one of which is the mid element's pair. 
            Ignoring the mid element's pair, there will be an odd number of elements to the left.
            So the single element must be to the left.

            
            Conversely, if the mid element is the Nth element where N is even and it is the first of its pair,
            that means there are an odd number of elements to the left, one of which is the single element.
            So the single element must be to the left.

            If the mid element is the second of its pair,
            that means there are an odd number of elements to the left, one of which is the mid element's pair.
            Ignoring the mid element's pair, there will be an even number of elements to the left which are properly paired.
            So the single element must be to the right.
            """
            if isOdd(mid + 1):
                if isRightNeighbourMe:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if isRightNeighbourMe:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1