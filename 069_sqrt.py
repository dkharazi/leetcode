# -*- coding: utf-8 -*-
"""
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since we want to return an integer, the decimal part will be truncated.

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
    # py3 is fine. maybe py2 is 32 bit.
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(x // 2, -1, -1):
            if i * i > x:
                return i - 1

    # binary search
    def mySqrt(self, x):
        left = 1    # or 0
        right = x   # or x/2 + 1
        while left <= right:
            mid = (right - left) / 2 + left
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:   # mid * mid > x:
                right = mid - 1
        return right

    # Newton method
    def mySqrt(self, x):
        n = x
        while n * n > x:
            n = (n + x / n) / 2
        return n


if __name__ == '__main__':
    print (Solution().mySqrt(9))
    print (Solution().mySqrt(2147395599))
