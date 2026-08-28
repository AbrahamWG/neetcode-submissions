from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        1) use deque
        2) while len(q) < k, when insert new max number, pop the back until hit a number bigger than it
        3) if len(q) == k, we have to pop the top max number
        4) store max number each iteration
        """
        res = []
        q = deque()
        l, r = 0, 0 # l, r are index, not values

        # r = 2, l = 0, q = [3]
        while r < len(nums):
            # if new number is bigger than the smallest in the window, pop the back of q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # add the index of the new number to q
            q.append(r)
            # if the index of max value is outside the window, left boundary
            if q[0] < l:
                q.popleft()
            # if we hit k window size, append max to res
            if r >= k - 1:
                l += 1 
                res.append(nums[q[0]])     
            r += 1
                  
        return res

        # time O(n)
        # space O(k)