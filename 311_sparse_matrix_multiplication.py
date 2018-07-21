# -*- coding: utf-8 -*-

'''
Sparse Matrix Multiplication
============================
Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.
Example:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''

class Solution(object):
    '''算法思路：
    中规中矩的矩阵乘法
    结果：TLE
    '''
    def multiply(self, A, B):
        if not A or not B:
            return []
        return [[
            sum(map(lambda x: x[0] * x[1], zip(A[i], [row[j] for row in B])))
            for j in range(len(B[0]))]
            for i in range(len(A))
            ]


class Solution(object):
    """
    https://www.jianshu.com/p/270245769c2a
    Sparse matrix意思是0很多的矩阵，所以这道题为了不TLE要检查0及时跳过，毕竟乘法里边有一个乘数为零就没有意义再乘了.
    """
    def multiply(self, A, B):
        row = len(A)
        col = len(B[0])
        n = len(A[0])
        C =[ [0 for i in range(col)] for j in range(row) ]
        for i in range(row):
            for j in range(col):
                for k in range(n):
                    if A[i][k] == 0 or B[k][j] == 0:
                        continue
                    else:
                        C[i][j] += A[i][k] * B[k][j]
        return C


    def multiply(self, A, B):
        row = len(A)
        col = len(B[0])
        n = len(A[0])
        C =[ [0 for i in range(col)] for j in range(row) ]
        for i in range(row):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(col):
                        if B[k][j] != 0:
                            C[i][j] += A[i][k] * B[k][j]
        return C


A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

s = Solution()
print(s.multiply(A, B))
