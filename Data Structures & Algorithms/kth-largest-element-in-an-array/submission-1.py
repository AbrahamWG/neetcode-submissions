import heapq as hq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # kth largest so negate to get max
        h = [-n for n in nums]
        hq.heapify(h)
        while k > 1:
            hq.heappop(h)
            k -= 1
        return -hq.heappop(h)