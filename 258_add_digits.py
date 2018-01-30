# 258. Add Digits
#
#  Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
#  For example:
#
#      Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
#  Follow up:
#      Could you do it without any loop/recursion in O(1) runtime?
#

class Solution(object):
    # recursive
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        return self.addDigits(sum(int(d) for d in str(num)))

        # num = sum(int(d) for d in str(num))
        # need return here
        # return self.addDigits(num)

    # iterative
    def addDigits2(self, num):
        while num >= 10:
            num = num // 10 + num % 10
        return num

    # http://bookshadow.com/weblog/2015/08/16/leetcode-add-digits/
    def addDigits(self, num):
        if num == 0:
            return 0
        return (num - 1) % 9 + 1

print Solution().addDigits(38)
print Solution().addDigits(8)
print Solution().addDigits(0)
print Solution().addDigits(138)

