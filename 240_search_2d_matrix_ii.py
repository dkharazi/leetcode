# 240. Search a 2D Matrix II
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

# http://www.tangjikai.com/algorithms/leetcode-240-search-a-2d-matrix-ii
# http://www.cnblogs.com/yrbbest/p/5005947.html
#
# For each number, its below number is larger and left is smaller.
# The top-left number is the smallest and the bottom-right is the largest in the matrix,
# so the top-right number is the middle number, which the starting point to search.
# If matrix[i][j] < target: i ++; if matrix[i][j] > target: j--
#
# Complexity:
# O(m + n) time
# O(1) space


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        m = len(matrix)     # row
        n = len(matrix[0])  # col

        i, j = 0, n-1       # bin search starting point:
                            # upper right corner: (i, j) = (0, n-1)

        while i < m and j > 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False



