class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        ret = 0

        for i in range(len(s)):
            ret += expand(i, i)
            ret += expand(i, i + 1)

        return ret