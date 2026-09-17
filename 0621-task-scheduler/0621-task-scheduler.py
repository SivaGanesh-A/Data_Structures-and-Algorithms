import heapq
from collections import Counter
from collections import deque
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []

        for task, count in freq.items():
            heapq.heappush(heap, (-count, task))
        
        cooldown = deque()
        time = 0

        while heap or cooldown:
            while cooldown and cooldown[0][1] <= time:
                count, available_time, task = cooldown.popleft()
                heapq.heappush(heap, (count, task))
            if heap:
                count, task = heapq.heappop(heap)
                count += 1

                if count != 0:
                    cooldown.append((count, time+n+1, task))
            time += 1
        return time