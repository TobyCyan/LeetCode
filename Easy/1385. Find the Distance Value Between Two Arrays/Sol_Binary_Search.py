class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n = len(arr2)
        count = 0
        
        arr2.sort()

        # The idea is that abs(first - second) <= d means first - d <= second <= first + d
        # So just search for any number in arr2 within the range [first - d, first + d]
        def binarySearch(lB, hB):
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr2[mid] >= lB and arr2[mid] <= hB:
                    return True
                if arr2[mid] < lB:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return False

        for num in arr1:
            found = binarySearch(num - d, num + d)
            if not found:
                count += 1
        
        return count