from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_c = sorted(citations, reverse=True)

        def check(value):
            return sorted_c[value - 1] >= value

        l, r = 1, len(citations)
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
