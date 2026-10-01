"""
Definition of Interval:
class Interval(object) :
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        i = 0
        n = len(intervals)

        while i + 1 < n:
            start = intervals[i].start
            end = intervals[i].end

            if intervals[i + 1].start < end:
                return False
            i += 1

        return True