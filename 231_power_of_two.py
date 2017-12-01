# 231. Power of Two
# Given an integer, write a function to determine if it is a power of two.

# http://www.cnblogs.com/grandyang/p/4623394.html
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt = 0
        while n > 0:
            cnt += (n & 1)
            n >>= 1

        return cnt == 1

print Solution().isPowerOfTwo(1)
