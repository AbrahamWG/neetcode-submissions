class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[l] or nums[r] < target or l == m == r and nums[l] != target:
                return -1
            if nums[m] == target:
                return m
            if nums[l] <= target and target < nums[m]:
                r = m - 1
                m = (r + l) // 2
            elif nums[m] < target and target <= nums[r]:
                l = m + 1
                m = (r + l) // 2