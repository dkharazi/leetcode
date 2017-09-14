# 201. Bitwise AND of Numbers Range
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
# http://www.cnblogs.com/grandyang/p/4431646.html
# The problem is all about finding the longest common sequence between n and m
# starting from the most significant bit,
# since all the following bits will flip for at least once and the AND result will be 0.


class Solution(object):
    def __init__(self):
        self.INT_MAX = 2147483647

    # brutal force MemoryError
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m
        for i in range(m + 1, n + 1):
            res &= i
        return res

    # use mask
    def rangeBitwiseAnd(self, m, n):
        b = self.INT_MAX
        while (b & m) != (b & n):
            b <<= 1

        return b & m

    def rangeBitwiseAnd(self, m, n):
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count


if __name__ == '__main__':
    print Solution().rangeBitwiseAnd(5, 7)
