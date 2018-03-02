"""
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

from pprint import pprint


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # unpack a list of arguments as positional arguments
        # then zip from the lists
        # returns list of tuples (py2), but leetcode accepts it
        # >>> matrix
        # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # >>> matrix[::-1]
        # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        # >>> zip(*matrix[::-1])
        # [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

        matrix[:] = zip(*matrix[::-1])
        # or
        # matrix[:] = zip(*matrix.reverse())

    # http://www.cnblogs.com/zuoyuan/p/3772978.html
    # rotate 90 clockwise = transpose + reverse each row
    def rotate(self, matrix):
        n = len(matrix)
        # transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row
        for i in range(n):
            matrix[i].reverse()

    # list comprehension
    def rotate(self, matrix):
        matrix[:] = [[row[i] for row in matrix[::-1]]
                     for i in range(len(matrix))]


if __name__ == '__main__':
    image = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print image
    print

    # print before rotate
    for i in image:
        print i
    print

    Solution().rotate(image)

    # print after rotate
    for i in image:
        print i
