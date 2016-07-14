# Given an integer n, count the total number of digit 1 appearing
# in all non-negative integers less than or equal to n.
#
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers:
#  1, 10, 11, 12, 13.
#

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int

        """
        # sum all the '1's inside the n numbers
        count = 0
        for i in range(1, n+1): # count including n
            count += self.numberOfDigitOne(i)

        return count

    def numberOfDigitOne(self, n):
        """
        function to count number of digit ones in a number n.

        mod by 10 to test if 1st digit is 1;
        then divide by 10 to get next digit;
        next test if next digit is 1.
        """

        result = 0
        while n:
            if n % 10 == 1:
                result += 1
            n = n / 10

        return result

if __name__ == "__main__":
    print Solution().countDigitOne(13)

