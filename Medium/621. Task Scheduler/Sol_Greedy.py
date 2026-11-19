from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        cooldown = deque()

        for cpu in freq:
            heapq.heappush(heap, (-freq[cpu], cpu))
        
        time = 0
        while heap or cooldown:
            while cooldown and cooldown[0][2] <= time:
                cpu, remaining, _ = cooldown.popleft()
                heapq.heappush(heap, (remaining, cpu))
            
            if heap:
                top, cpu = heapq.heappop(heap)
                top += 1
                if top < 0:
                    cooldown.append((cpu, top, time + n + 1))
            
            time += 1

        return time
