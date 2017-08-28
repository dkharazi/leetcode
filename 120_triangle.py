# -*- coding: utf-8 -*-
# 120. Triangle
#
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.


class Solution(object):
    def minimumTotal(self, triangle):
        """
        https://shenjie1993.gitbooks.io/leetcode-python/120%20Triangle.html

        典型的动态规划问题，先将问题转化一下，把每一行的数列都左对齐，如下：
        [
          [2],
          [3,4],
          [6,5,7],
          [4,1,8,3]
        ]
        可以看出来，其实上一行到下一行就两个选择，横坐标不变或加一。
        dp[i]表示从底层到这一层的第i个元素所有路径中最小的和。
        递推关系就是 dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])，
        即下一行与它相邻的两个节点中和比较小的再加上它自己的值。

        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


if __name__ == "__main__":
    assert Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]) == 11
