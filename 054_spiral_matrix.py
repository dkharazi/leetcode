"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3769829.html
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        direct = 0  # 0: go right   1: go down  2: go left  3: go up
        res = []

        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            elif direct == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif direct == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            elif direct == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right:
                return res
            direct = (direct + 1) % 4


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    print Solution().spiralOrder(A)
