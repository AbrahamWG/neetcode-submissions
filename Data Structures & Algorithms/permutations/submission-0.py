class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Use index i in the start
        # use rest, 
        ans = []

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return ans
