class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        m, n = len(arr1), len(arr2)
        count = 0
        for i in range(m):
            first = arr1[i]
            found = False
            for j in range(n):
                second = arr2[j]
                if abs(first - second) <= d:
                    found = True
                    break
            if not found:
                count += 1
        return count