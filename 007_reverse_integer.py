"""
7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""


class Solution(object):
    MIN = - 2 ** 31
    MAX = 2 ** 31 - 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """


        result = 0
        sign = 1

        digit_list = list(str(x))
        if list(str(x))[0]  == '-':
            del digit_list[0]
            sign = -1

        for index, digit in enumerate(digit_list):
            result += int(digit) * 10 ** index

        result *= sign

        if result < self.MIN or result > self.MAX:
            return 0

        return result

    # http://www.cnblogs.com/zuoyuan/p/3777730.html
    def reverse2(self, x):
        answer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            answer = answer * 10 + x % 10
            x /= 10

        if sign * answer < self.MIN or sign * answer > self.MAX:
            return 0

        return sign * answer


if __name__ == '__main__':
    print Solution().reverse(-120)
    print Solution().reverse(100)
    print Solution().reverse(3)