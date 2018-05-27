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

    def isPowerOfTwo(self, n):
        """
        check if n can be divided by 2. If yes, divide n by 2 and check it repeatedly,
        until it can not be divided by 2. then check if it equals 1.
        """
        if n == 0:
            return False
        while n %2 == 0:
            n /= 2
        return n == 1

    # bit operation
    # http://bookshadow.com/weblog/2015/07/06/leetcode-power-of-two/
    def isPowerOfTwo(self, n):
        """
        如果一个整数是2的幂，那么它的二进制形式最高位为1，其余各位为0
        If an integer is power of 2, there is a single bit in the binary representation of n.
        n & n - 1 removes the left most bit of n.
        e.g. 16 = b10000, 16 - 1 = b01111, and 16 & 16 - 1 = b10000 & b01111 = 0, also 16 != 0,
        based on these facts there is only one bit in b10000, so 16 is power of 2.
        """
        return n > 0 and n & (n - 1) == 0
        # return n > 0 and not (n & n-1)

print Solution().isPowerOfTwo(1)
