# -*- coding: utf-8 -*-
#  221. Maximal Square
#
#  Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Return 4.
#


class Solution(object):
    # http://bookshadow.com/weblog/2015/06/03/leetcode-maximal-square/
    # 动态规划（Dynamic Programming）
    #
    # 状态转移方程：
    #
    # dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1
    #
    # 上式中，dp[x][y]表示以坐标(x, y)为右下角元素的全1正方形矩阵的最大长度（宽度）
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # dp = [[0] * n for _ in range(m)]
        dp = [[0 for _ in range(n)] for __ in range(m)]

        ans = 0
        for x in range(m):
            for y in range(n):
                dp[x][y] = int(matrix[x][y])
                if x and y and dp[x][y]:  # if not on boundaries, and not 0
                    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1
                # remember size of largest square so far
                ans = max(ans, dp[x][y])
        return ans * ans

    # when iterating the first row or first column,
    # the formula for dp(i, j) is checking for values out of bounds.
    # By shifting the whole dp to the right and bottom by 1
    # and adding a padding of 0's to the 1st row and 1st column,
    # it makes the formula work without checking for boundaries.
    #
    # Time complexity : O(mn). Single pass.
    #
    def maximalSquare(self, matrix):
        res = 0
        if not matrix:
            return res * res
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        # dp shifted right and bottom
        for x in range(1, m + 1):
            for y in range(1, n + 1):
                if matrix[x - 1][y - 1] == '1':
                    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1
                    res = max(res, dp[x][y])
        return res * res
