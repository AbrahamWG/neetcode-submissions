class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right)
        
        start, end = 0, 0

        for i in range(len(s)):
            for l, r in (expand(i, i), expand(i, i + 1)):
                # keep the longer window
                if r - l > end - start:
                    start, end = l, r

        return s[start:end]
        