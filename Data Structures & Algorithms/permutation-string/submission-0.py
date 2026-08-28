class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # have 2 dictionaries for s1 and s2 with each letter as a key and number of occurences as the value
        # s1 is permutation of s2 if both dict match
        # the sliding window size at most be len(s1)
        # 2 pointers: move the right pointer until size == len(s1), then left pointer begin to move 
        # track number of matches we have right now, return True if matches = len(s1)

        d1, d2 = {}, {}
        matches = 0

        # populate d1
        for c in s1:
            if c not in d1:
                d1[c] = 0
            d1[c] += 1

        l, r = 0, 0
        while r < len(s2):
            # break case
            if matches == len(d1):
                return True
            new_char = s2[r]
            # if new char not in d2, add it
            if new_char not in d2:
                d2[new_char] = 0
            d2[new_char] += 1
            # right amount += 1 match
            if new_char in d1:
                if d1.get(new_char) == d2.get(new_char):
                    matches += 1
                # too many occurences -= 1 match
                elif d1.get(new_char) + 1 == d2.get(new_char):
                    matches -= 1
            # not match, move pointers, left move if hit size limit
            last_char = s2[l]
            if (r - l) == len(s1):
                # if it was matching before, matches -= 1
                if last_char in d1 and d2.get(last_char) == d1.get(last_char):
                    matches -= 1
                d2[last_char] -= 1
                # if now matching, matches += 1
                if last_char in d1 and d2.get(last_char) == d1.get(last_char):
                    matches += 1
                l += 1 
            r += 1

        return matches == len(d1)

        # time O(n)
        # space O(1)