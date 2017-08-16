"""
29. Divide Two Integers


Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3779359.html
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0

        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res

    # http://blog.csdn.net/u013291394/article/details/50423914
    def divide(self, dividend, divisor):
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = -1
        else:
            flag = 1

        c, sub = 1, abs(divisor)
        e, s = abs(dividend), abs(divisor)

        res = 0
        while e >= s:
            if e >= sub:
                e -= sub
                res += c
                sub <<= 1  # sub *= 2
                c <<= 1  # c *= 2
            else:
                sub >>= 1  # sub /= 2
                c >>= 1  # c /= 2

        res *= flag

        return min(max(res, -2147483648), 2147483647)

if __name__ == '__main__':
    print Solution().divide(5, 3)