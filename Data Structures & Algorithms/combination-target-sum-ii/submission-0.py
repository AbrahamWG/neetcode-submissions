class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # what does one call decide
        # what are the choices
        # when am i done
        # what do i undo

        candidates.sort() # O(n)
        res = []
        comb = []

        def dfs(i, running_sum):
            # met target, append comb, stop loop
            if running_sum == target:
                res.append(comb[:]) # append a copy of comb, dfs should not treat as local
                return 
            # no more candidates or too big, stop loop
            elif i == len(candidates) or running_sum > target:
                return
            # running_sum still < target
            else:
                # quick return
                if running_sum + candidates[i] > target:
                    return
                # 1st choice: use cand i
                comb.append(candidates[i])
                running_sum += candidates[i]
                dfs(i + 1, running_sum)
                # 2nd choice: don't use cand i
                running_sum -= comb.pop()
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i += 1
                dfs(i + 1, running_sum)

        dfs(0, 0)
        return res