import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # max 2 stones, y is 1st, x is 2nd
        # end game at 1 stone left, return it
        # use negatives to convert to max heap

        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)
            if x != y:
                heapq.heappush(h, x-y)

        if h: 
            return -heapq.heappop(h)
        return 0