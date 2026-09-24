import heapq as hq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = [(x*x + y*y, i) for i, (x, y) in enumerate(points)]
        # pick top k
        hq.heapify(distances)
        ans = []
        top_k = 0
        while top_k < k:
            ans.append(points[hq.heappop(distances)[1]])
            top_k += 1

        return ans