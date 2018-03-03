# -*- coding: utf-8 -*-
"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Author: gengwg
"""

from collections import Counter

l = [(1, 3), (2, 6), (8, 10), (15, 18)]

# flatten the list
flat = [x for _ in l for x in _]
# sort set flatted list (ssf)
ssf = sorted(set(flat))

to_remove = []

c = Counter(flat)
for x in c:
    # remove all elements appeared more than once,
    # but only in the middle,
    # which would be the border of two intervals
    if c[x] > 1 and x in ssf[1:-1]:
        to_remove.append(x)

# loop over all intervals
# if any x in ssf is within any interval
# it needs to be removed
for x in ssf:
    for y in l:
        if y[0] < x < y[1]:
            to_remove.append(x)

# remove above selected
for x in set(to_remove):
    ssf.remove(x)

# zip even numbers with odd numbers
# the final result are guarrantted to be even numbers
# due to the intervals are pairs..
print zip(ssf[0::2], ssf[1::2])


# --------------------
# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str((self.start, self.end))


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]

        http://www.cnblogs.com/zuoyuan/p/3782028.html
        解题思路：
        先将区间按照每个start的值来排序，
        排好序以后判断一个区间的start值是否处在前一个区间中，
        如果在前一个区间中，那么合并；
        如果不在，就将新区间添加。
        """
        intervals.sort(key=lambda x: x.start)
        length = len(intervals)
        res = []
        for i in range(length):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size - 1].start <= intervals[i].start <= res[size - 1].end:
                    res[size - 1].end = max(intervals[i].end, res[size - 1].end)
                else:
                    res.append(intervals[i])
        return res

    # scanning line algorithm
    # https://gengwg.blogspot.com/2018/03/leetcode-56-merge-intervals.html
    def merge(self, intervals):
        if not intervals:
            return []
        # sort according to x.start
        intervals.sort(key=lambda x: x.start)
        res = []
        start = intervals[0].start
        end = intervals[0].end
        for interval in intervals:
            if interval.start <= end:  # overlaps
                end = max(end, interval.end)
            else:
                res.append(Interval(start, end)) # add current merged interval
                # reset start and end to new interval
                start = interval.start
                end = interval.end
        res.append(Interval(start, end))    # must not miss last interval!
        return res


if __name__ == '__main__':
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    for interval in intervals:
        print interval,
    print
    for interval in Solution().merge(intervals):
        print interval,
