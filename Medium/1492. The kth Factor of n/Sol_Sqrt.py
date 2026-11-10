from math import sqrt, ceil, floor

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def isFactor(n, i):
            return n % i == 0
        
        if k == 1:
            return 1
        
        count = 1
        root = sqrt(n)
        for i in range(2, ceil(root)):
            if isFactor(n, i):
                count += 1
            if count == k:
                return i
        
        for i in range(floor(root), 0, -1):
            if isFactor(n, n // i):
                count += 1
            if count == k:
                return n // i
        
        return -1