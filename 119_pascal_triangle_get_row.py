# -*- coding: utf-8 -*-
# 119. Pascal's Triangle II
#
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in xrange(1, rowIndex + 1):
            result = [1] + [result[j - 1] + result[j] for j in xrange(1, i)] + [1]
        return result + [1]

    # https://shenjie1993.gitbooks.io/leetcode-python/119%20Pascal's%20Triangle%20II.html
    def getRow(self, rowIndex):
        # on kth row, has k+1 elements
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                res[i - j] += res[i - j - 1]
                # print i, res
        return res


class Solution2(object):
    def getRow(self, rowIndex):
        result = [0] * (rowIndex + 1)
        for i in xrange(rowIndex + 1):
            old = result[0] = 1
            for j in xrange(1, i + 1):
                old, result[j] = result[j], old + result[j]
        return result


if __name__ == "__main__":
    print Solution().getRow(4)
