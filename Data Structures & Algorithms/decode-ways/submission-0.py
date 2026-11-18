class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def helper(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            
            ways = helper(i+1)
            if i + 1 < len(s) and int(s[i: i + 2]) <= 26:
                ways += helper(i + 2)
            
            memo[i] = ways
            return ways
            
        return helper(0)