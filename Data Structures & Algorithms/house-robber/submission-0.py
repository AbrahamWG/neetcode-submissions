class Solution:
    def rob(self, nums: list[int]) -> int:
        # 2 decision:
        # best[i] = max(best[i-2] + nums[i], best[i-1])
        if len(nums) == 1:
            return nums[0]
        best = [0 for _ in range(len(nums))]
        best[0], best[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            best[i] = max(best[i-2] + nums[i], best[i-1])
        return best[-1]
    
        # nums = [2,7,9,3,1]
        # best[0] = 2
        # best[1] = 7
        # best[2] = 2 + 9 = 11
        # best[3] = best[2] = 11
        # best[4] = 12
        # return 12