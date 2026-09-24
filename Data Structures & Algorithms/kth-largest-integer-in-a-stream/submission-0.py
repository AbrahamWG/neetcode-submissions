import heapq     

class KthLargest:
    # return k-th highest test core, len(q) - k 
    # only care about the k highest one, no need to store all
    # min heap store k largest scores
    # h[0] is min


    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)

        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]