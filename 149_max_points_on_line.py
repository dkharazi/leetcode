# -*- coding: utf-8 -*-
# 149 Max Points on a Line
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


from decimal import *


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    # tle
    def maxPoints(self, points):
        """
        http://www.cnblogs.com/zuoyuan/p/3760628.html
        解题思路：
        找到平面上在一条直线上最多的点。
        点在同一条直线上意味着这些点的斜率是一样的，
        那么可以考虑使用哈希表来解决，{斜率：[点1，点2]}这样的映射关系。
        这里有几个需要考虑的要点：
        1，有可能是斜率无穷大。
        2，有可能有相同的点，比如[(1,2),(1,2)]。

        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if length < 3:
            return length

        res = -1
        for i in range(length):
            slope = {'inf': 0}
            samePointsNum = 1
            for j in range(length):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    # k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    # main will give wrong answer if not use decimal
                    k = (Decimal(points[i].y) - Decimal(points[j].y)) / (Decimal(points[i].x) - Decimal(points[j].x))

                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
                else:
                    samePointsNum += 1
            # print slope, samePointsNum
            res = max(res, max(slope.values()) + samePointsNum)
        return res


if __name__ == '__main__':
    # this will give 3 if not using decimal class
    print Solution().maxPoints([Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)])
