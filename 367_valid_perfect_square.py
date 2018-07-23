# 367. Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
#
# Example 2:
#
# Input: 14
# Returns: False
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        r = (num >> 1) + 1
        while l <= r:
            m = l + ((r-l )>> 1)
            mul = m ** 2
            if mul == num:
                return True
            elif mul > num:
                r = m - 1
            else:
                l = m + 1
        return False

sol = Solution()
print(sol.isPerfectSquare(16))
print(sol.isPerfectSquare(14))

