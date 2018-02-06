# 264. Ugly Number II
#
# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include
# 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it
# includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.

class Solution(object):
    # brute force
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

    # https://www.hrwhisper.me/leetcode-ugly-number-i-ii/
    # https://www.youtube.com/watch?v=ZG86C_U-vRg
    def nthUglyNumber(self, n):
        ugly = [1] * n       # ugly[0] = 1; first ugly is 1.
        i2 = i3 = i5 = 0    # index for candiate multiply by 2,3,5 separately
        for i in range(1, n):
            # find min among all candidates
            ugly[i] = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            # if processed by any factor, increment it.
            # note do not use elif: need increment all min.
            if ugly[i] == ugly[i2] * 2:   i2 += 1
            if ugly[i] == ugly[i3] * 3:   i3 += 1
            if ugly[i] == ugly[i5] * 5:   i5 += 1
        return ugly[n-1]

if __name__ == "__main__":
    print Solution().nthUglyNumber(10)
    print Solution().nthUglyNumber(1500)
