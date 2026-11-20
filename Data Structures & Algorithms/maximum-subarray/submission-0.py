class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = nums[0]
        running_sum = 0

        for i in range(len(nums)):
            if running_sum < 0:
                running_sum = nums[i]
            else: 
                running_sum += nums[i]
            best_sum = max(best_sum, running_sum)
        return best_sum