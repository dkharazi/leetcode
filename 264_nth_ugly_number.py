# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include
# 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it
# includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5

        return num == 1

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        number = 0
        uglyFound = 0
        while uglyFound < n:
            number += 1
            if self.isUgly(number):
                uglyFound += 1

        return number

if __name__ == "__main__":
    print Solution().nthUglyNumber(1500)
