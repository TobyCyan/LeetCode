import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def distance_sqr(point):
            x, y = point[0], point[1]
            return x ** 2 + y ** 2
        
        heap = []
        for point in points:
            heapq.heappush(heap, (distance_sqr(point), point))
        
        result = []
        for _ in range(k):
            _, top = heapq.heappop(heap)
            result.append(top)
        
        return result