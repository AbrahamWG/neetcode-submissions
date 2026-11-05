class Solution:
    def rob(self, nums: List[int]) -> int:
        # run the recursion twice on i=0 and i=1
        # run i = 0 stop at i-2
        # at house i, return max(sum from i-1 + rob(i+1), sum from i-2 + i + rob(i+2)))
        # time: O(2^n) since every step we do 2 recursion calls
        # space: O(2^n) the max depth recurison gets
        # use memo top down

        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev2, prev1 = 0, 0
            for money in arr:
                # skip house or rob it plus 2 back
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        # circle: drop last or first house
        return max(helper(nums[:-1]), helper(nums[1:]))