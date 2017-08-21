# -*- coding: utf-8 -*-
"""
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

http://www.cnblogs.com/zuoyuan/p/3775852.html

解题思路：
实现开平方函数。
这里要注意的一点是返回的时一个整数。
通过这一点我们可以看出，很有可能是使用二分查找来解决问题的。
这里要注意折半查找起点和终点的设置。起点i=1；终点j=x/2+1；
因为在(x/2+1)^2 > x，所以我们将折半查找的终点设为x/2+1。
"""


class Solution(object):
    # MemoryError
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(x / 2, -1, -1):
            if i * i > x:
                return i - 1

    def mySqrt(self, x):
        if x == 0:
            return 0
        # note start, end positions
        i, j = 1, x / 2 + 1
        while i <= j:
            c = (i + j) / 2
            if c * c == x:
                return c
            elif c * c > x:
                j = c - 1
            else:  # c * c < x
                i = c + 1
        return j


if __name__ == '__main__':
    print Solution().mySqrt(9)
    print Solution().mySqrt(2147395599)
