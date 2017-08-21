# Given a non-negative number represented as an array of digits, plus one to the number.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
#


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        # another way of traversing list from back
        # reversed(range(N)) == range(N-1, -1, -1)
        # e.g.:
        # In[113]: list(reversed(range(9)))
        # Out[113]: [8, 7, 6, 5, 4, 3, 2, 1, 0]
        #
        # In[114]: list(range(8, -1, -1))
        # Out[114]: [8, 7, 6, 5, 4, 3, 2, 1, 0]
        # for i in reversed(xrange(len(digits))):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] / 10  # quotient is 1 or 0
            digits[i] %= 10  # remainder

        # msb carry, 1 or 0
        if carry:
            digits = [1] + digits

        return digits


if __name__ == "__main__":
    print Solution().plusOne(digits=[9, 9, 9, 9])
    print Solution().plusOne(digits=[9, 9, 9, 2])
