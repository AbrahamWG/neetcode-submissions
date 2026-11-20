class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        running_sum = 0
        min_size = 0

        for r in range(len(nums)):
            running_sum += nums[r]
            if running_sum < target:
                continue

            while running_sum >= target:
                if not min_size: 
                    min_size = r - l + 1
                min_size = min(min_size, r - l + 1)
                running_sum -= nums[l]
                l += 1

        return 0 if not min_size else min_size
