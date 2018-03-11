"""
73. Set Matrix Zeroes

Given a m x n matrix,
if an element is 0,
set its entire row and column to 0.
Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # store 0 positions in a list
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    l.append((i, j))

        # set its row and column to 0.
        for x in l:
            # set column
            for i in range(len(matrix)):
                matrix[i][x[1]] = 0
            # set row
            for j in range(len(matrix[0])):
                matrix[x[0]][j] = 0

    # http://www.cnblogs.com/zuoyuan/p/3769698.html
    def setZeroes(self, matrix):
        row = [False for _ in range(len(matrix))]
        col = [False for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or col[j]:
                    matrix[i][j] = 0


if __name__ == '__main__':
    A = [
        [1, 0, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    Solution().setZeroes(A)
    import pprint
    pprint.pprint(A)
