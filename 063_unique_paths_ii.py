# -*- coding: utf-8 -*-
"""
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

https://shenjie1993.gitbooks.io/leetcode-python/063%20Unique%20Paths%20II.html

思路跟 Unique Paths 是一样的，
不过要分类讨论一下障碍的情况，
如果当前格子是障碍，那么到达该格子的路径数目是0，
因为无法到达，如果是普通格子，那么由左边和右边的格子相加。
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # if start is 1, no path exists
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for __ in range(m)]
        dp[0][0] = 1

        # first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        # first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    assert Solution().uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]) == 2
