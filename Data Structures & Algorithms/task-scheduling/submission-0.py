import heapq as hq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count how many unique tasks
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        # greedy: run task with most frequencies
        h = [-c for c in count.values()]
        hq.heapify(h)
        # cooldown queue
        q = deque()
        time = 0
        # main loop
        while h or q:
            time += 1
            if h:
                c = hq.heappop(h) + 1
                if c != 0:
                    q.append((c, time + n))
            if q and q[0][1] == time:
                hq.heappush(h, q.popleft()[0])
        return time