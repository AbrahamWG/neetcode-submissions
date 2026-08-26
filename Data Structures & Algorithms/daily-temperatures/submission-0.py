class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for i in range(len(temperatures))]
        curr = 0
        
        while curr < len(temperatures):
            # compare temp today vs top of stack
            while stack and temperatures[curr] > temperatures[stack[-1]]:
                # curr index - popped index = duration of days
                ans[stack[-1]] = curr - stack[-1]
                stack.pop()
            stack.append(curr)
            curr += 1
        return ans