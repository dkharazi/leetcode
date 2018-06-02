# 304 Range Sum Query 2D - Immutable
#
# Given a 2D matrix matrix,
# find the sum of the elements inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).

# Example:

# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12

# Note:

#     You may assume that the matrix does not change.
#     There are many calls to sumRegion function.
#     You may assume that row1 ≤ row2 and col1 ≤ col2.

# http://bookshadow.com/weblog/2015/11/12/leetcode-range-sum-query-2d-immutable/

# 构造辅助二维数组sums

# sums[x][y]表示从0,0到x,y的子矩阵的和

# 利用容斥原理，可知：

# sumRange(row1, col1, row2, col2)
# = sums[row2][col2] + sums[row1 - 1][col1 - 1] - sums[row1 - 1][col2] - sums[row2][col1 - 1]

# 将辅助矩阵的行数和列数+1，可以简化对矩阵边界的处理。

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        self.sums = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] \
                + self.sums[i-1][j] - self.sums[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] \
                 - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
