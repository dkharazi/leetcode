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

    # TLE
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


    def uniquePaths(self, m: int, n: int) -> int:
        def compute_number_of_ways_to_xy(x, y):
            if x == y == 0:
                return 1

            if number_of_ways[x][y] == 0:
                ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x-1, y)
                ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y-1)
                number_of_ways[x][y] = ways_left + ways_top
            return number_of_ways[x][y]

        number_of_ways = [[0] * m for _ in range(n)]
        return compute_number_of_ways_to_xy(n-1, m-1)

    # a analytical way is to use the fact that each path from (0,0) to (n-1,m-1)
    # is a sequence of m-1 horizontal steps and n-1 vertical steps.
    # there are C(n+m-2,n-1) = C(n+m-2, m-1) = (n+m-2)! / ((n-1)! * (m-1)!)
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        return int(math.factorial(n+m-2) / (math.factorial(n-1) * math.factorial(m-1)))

if __name__ == '__main__':
    print(Solution().uniquePaths(4, 7))
    print(Solution().uniquePaths(5, 5))  # 70
