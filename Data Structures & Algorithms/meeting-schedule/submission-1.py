"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if there is overlap between start and end with other meeting return False
        # 1. sort and traverse from the earliest starting point of a meeting
        # 2. end of the first meeting signifies whether the second meeting can start or not
        # time: O(n log n) for sort and one pass
        # space: O(1) edit in place, earliest availability
        if not intervals:
            return True

        intervals.sort(key=lambda interval: interval.start)
        for i in intervals:
            print(i.start, i.end)
        available = 0
        for i in intervals:
            if not available:
                available = i.end
                continue
            if i.start < available:
                return False
            available = i.end
        return True