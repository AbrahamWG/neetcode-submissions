import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # step 1, count each task
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1

        # step 2, max heap of counts
        h = [-c for c in count.values()]
        heapq.heapify(h)

        # step 3, cooldown queue and timer
        q = deque()
        time = 0

        # step 4, one loop = one interval
        while h or q:
            time += 1
            if h:
                c = heapq.heappop(h) + 1
                if c != 0:
                    q.append((c, time + n))

            # step 5, release a task when its cooldown ends
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])

        return time