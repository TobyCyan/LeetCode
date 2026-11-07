from random import random

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def distance_sqr(point):
            x, y = point[0], point[1]
            return x ** 2 + y ** 2
        
        def partition(l, r, arr):
            p = random.randint(l, r)
            pivot = arr[p]
            lP = l
            arr[p], arr[r] = arr[r], arr[p]
            for rP in range(l, r):
                if distance_sqr(arr[rP]) < distance_sqr(pivot):
                    arr[rP], arr[lP] = arr[lP], arr[rP]
                    lP += 1
            arr[r], arr[lP] = arr[lP], arr[r]
            return lP
        
        def quickSelect(k, l, r, arr):
            if l > r:
                return
            
            pivotIdx = partition(l, r, arr)

            if pivotIdx == k:
                return
            
            if pivotIdx > k:
                quickSelect(k, l, pivotIdx - 1, arr)
                return

            quickSelect(k, pivotIdx + 1, r, arr)
        
        n = len(points)
        quickSelect(k - 1, 0, n - 1, points)
        
        return points[:k]