class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i : i[0])
        
        result = []
        start, furthest = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= furthest:
                furthest = max(furthest, curr[1])
            else:
                merged = [start, furthest]
                result.append(merged)

                start, furthest = curr[0], curr[1]

        result.append([start, furthest])

        return result
