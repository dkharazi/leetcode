"""
59. Spiral Matrix II

Given an integer n,
generate a square matrix filled with elements from 1 to n^2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []

        matrix = [[0 for i in range(n)] for j in range(n)]

        up = 0
        down = n - 1
        left = 0
        right = n - 1
        direct = 0
        count = 0

        while True:

            if direct == 0:  # go right
                for i in range(left, right + 1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            if direct == 1:  # go down
                for i in range(up, down + 1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            if direct == 2:  # go left
                for i in range(right, left - 1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if direct == 3:  # go up
                for i in range(down, up - 1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n * n:  # break condition
                return matrix
            direct = (direct + 1) % 4   # increment direct base 4


if __name__ == '__main__':
    print Solution().generateMatrix(3)
