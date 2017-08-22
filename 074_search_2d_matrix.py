"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""


class Solution(object):
    # combine into one array, then use binary search
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        nums = []
        for x in matrix:
            nums += x

        i = 0;
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False

    # http://www.cnblogs.com/zuoyuan/p/3770061.html
    def searchMatrix(self, matrix, target):
        i = 0;
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False


if __name__ == '__main__':
    A = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    # A = [[]]
    print Solution().searchMatrix(A, 3)
