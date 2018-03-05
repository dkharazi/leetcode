# -*- coding: utf-8 -*-
"""
57. Insert Interval

Given a set of non-overlapping intervals,
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

http://www.cnblogs.com/zuoyuan/p/3782048.html
解题思路：
最简单的方法是将要插入的区间和原来的区间合在一起排序，
然后按照merge intervals的方法来编程。

"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size - 1].start <= intervals[i].start <= res[size - 1].end:
                    res[size - 1].end = max(intervals[i].end, res[size - 1].end)
                else:
                    res.append(intervals[i])

        return res

    # https://gengwg.blogspot.com/2018/03/leetcode-57-insert-interval-ep86.html
    def insert(self, intervals, newInterval):
        l = []
        r = []
        start = newInterval.start
        end = newInterval.end
        for interval in intervals:
            # left intervals
            if interval.end < newInterval.start:
                l.append(interval)
            # right intervals
            elif interval.start > newInterval.end:
                r.append(interval)
            # overlapping intervals
            else:
                start = min(interval.start, start)
                end = max(interval.end, end)
        return l + [Interval(start,end)] + r