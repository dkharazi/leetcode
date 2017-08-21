# -*- coding: utf-8 -*-
"""
70. Climbing Stairs

You are climbing a stair case.
It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

http://www.cnblogs.com/zuoyuan/p/3753553.html

解题思路：

爬楼梯问题。
经典的动态规划问题。
每次上一个台阶或者两个台阶，问一共有多少种方法到楼顶。

这个实际上就是斐波那契数列的求解。
可以逆向来分析问题，如果有n个台阶，那么走完n个台阶的方式有f(n)种。
而走完n个台阶有两种方法，
先走完n-2个台阶，然后跨2个台阶；
先走完n-1个台阶，然后跨1个台阶。
所以f(n) = f(n-1) + f(n-2)。
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]  # same as dp[-1]


if __name__ == '__main__':
    print Solution().climbStairs(3)
