class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def is_palindrome(left, right):
            # two pointers moving inward
            while left < right:
                if s[left] != s[right]:
                    return False 
                left += 1
                right -= 1
            return True

        def backtrack(start):
            # base case: used the whole string
            if start == len(s):
                # TODO: add a copy of current to result
                result.append(current[:])
                return

            # try every possible end for the next piece
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    # choose
                    current.append(s[start:end+1])
                    # recurse on what's left
                    backtrack(end + 1)
                    # undo
                    current.pop()

        backtrack(0)
        return result