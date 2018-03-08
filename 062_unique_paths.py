# -*- coding: utf-8 -*-
"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
这道题就是一个动态规划，所以每一个位置的走法数量，就是其左边和上方的和。
因为只能右边和下方走，那么对于每一个格子，
其就只可能来自这两个方向，
那么其往某个格子过来，就正好带来对应的解法，
这里一共有两个，所以就是他们的和

状态转移方程为dp[i][j]=dp[i-1][j]+dp[i][j-1]。
http://www.cnblogs.com/zuoyuan/p/3785221.html1
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            list = [[1]]
        elif m == 1 and n > 1:
            list = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            list = [[1] for i in range(m)]
        else:
            list = [[0 for i in range(n)] for i in range(m)]
            for i in range(0, n):
                list[0][i] = 1
            for i in range(0, m):
                list[i][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    list[i][j] = list[i - 1][j] + list[i][j - 1]
        return list[m - 1][n - 1]

    # http://www.tangjikai.com/algorithms/leetcode-62-unique-path
    def uniquePaths(self, m, n):
        # m rows, n columns
        dp = [[1] * n for _ in range(m)]

        # index starting at 1 because we need refer to i-1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    print Solution().uniquePaths(4, 7)
