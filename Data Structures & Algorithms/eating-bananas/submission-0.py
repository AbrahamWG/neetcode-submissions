import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        
        binary search on k
        if k = 4 OK, then k = 5, 6, 7 OK
        if k = 3 NOT OK, then k = 2, 1, NOT OK
        k is sorted small to big, NOT OK to tipping point OK
        small = 1, big = max(piles)
        mid = big + small // 2
        if m OK, search lower half, else higher half

        """

        def loop(mid):
            hours = 0
            for i in piles:
                rounded = math.ceil(i / mid)
                hours += rounded
            return hours

        small, big = 1, max(piles)
        res = big

        while small <= big:
            mid = (small + big) // 2
            # lower pile, finish in time, try tighter 
            if loop(mid) <= h:
                res = mid
                big = mid - 1
            # higher pile, didnt finished in time
            elif loop(mid) > h:
                small = mid + 1

        return res