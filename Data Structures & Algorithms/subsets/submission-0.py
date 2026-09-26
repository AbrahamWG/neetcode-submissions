class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []

        def dfs(i): # i is the index of number we are deciding on
            if i == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            dfs(i + 1)

        dfs(0) # start
        return res


        