# -*- coding: utf-8 -*-
# 118. Pascal's Triangle
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    # 杨辉三角
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(numRows):
            result.append([])
            for j in xrange(i + 1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])

        return result

    # http://blog.csdn.net/coder_orz/article/details/51589254
    # 利用Python的map函数可以比较精简的实现该算法。
    # 这里用到一个小小的trick，即：
    # 每一行的结果可以由上一行和上一行的偏移相加得到。例如：
    #
    #     1 3 3 1 0
    #  +  0 1 3 3 1
    #  =  1 4 6 4 1

    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]

        # [:numRows] is in case numRows ==0
        # return res will return [[1]]. should be [].
        return res[:numRows]


if __name__ == "__main__":
    print Solution().generate(0)

    print "["
    numRows = 9
    i = numRows * 2
    for li in Solution().generate(numRows):
        i -= 1
        # print "{:>20},".format(li)
        print "{},".rjust(i).format(li)
    print "]"
