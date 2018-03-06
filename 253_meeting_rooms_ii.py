# 253. Meeting Rooms II
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        res = 0
        end = 0
        for i in range(len(intervals)):
            if starts[i] < ends[end]:
                res += 1
            else:
                end += 1
        return res


if __name__ == '__main__':
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print Solution().minMeetingRooms(intervals)
