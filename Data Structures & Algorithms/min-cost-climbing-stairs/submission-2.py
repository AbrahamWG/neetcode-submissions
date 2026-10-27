class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. each step either choose i+1 or i+2
        # 2. dp problem, store min cost until i-th
        # 3. if i already cache return it

        cache = {}

        def check(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = cost[i] + min(check(i+1), check(i+2))
            return cache[i]
        return min(check(0), check(1))