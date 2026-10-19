class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(i):
            # stop when
            if i == len(nums):
                res.append(path[:])
                return
            # use nums[i]
            path.append(nums[i])
            dfs(i+1)
            # dont use nums[i]
            path.pop()
            # skip all dups
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)

        dfs(0)
        return res

        # time: O(n * 2^n)