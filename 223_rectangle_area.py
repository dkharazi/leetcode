# -*- coding: utf-8 -*-
# 223. Rectangle Area
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner
# as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        两个矩形各自占的面积减去交叠部分的面积即可。
        所以重点是判断两个矩形是否交叠，以及求交叠部分的面积。
        求交叠部分的面积分为两步：求宽度和求高度，还要注意当不交叠时的负数情况要处理掉。
        http://blog.csdn.net/coder_orz/article/details/51679907
        """
        total = (C - A) * (D - B) + (G - E) * (H - F)
        if B >= H or E >= C or F >= D or A >= G:
            return total

        width = min(C, G) - max(A, E)
        height = min(D, H) - max(B, F)
        return total - width * height
