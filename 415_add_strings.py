# 415. Add Strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
#     The length of both num1 and num2 is < 5100.
#     Both num1 and num2 contains only digits 0-9.
#     Both num1 and num2 does not contain any leading zero.
#     You must not use any built-in BigInteger library or convert the inputs to integer directly.
#


class Solution(object):
    # https://leetcode.com/problems/add-strings/discuss/90436/Straightforward-Java-8-main-lines-25ms
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1:
            return num2

        if not num2:
            return num1

        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        digit = 0
        result = []

        while i >=0 or j >= 0 or carry != 0:
            digit = carry
            if i >=0:
                digit += int(num1[i])
                i -= 1
            if j >=0:
                digit += int(num2[j])
                j -= 1
            carry = digit // 10
            result.append(digit%10)


        return ''.join(str(e) for e in result[::-1])


sol = Solution()
print(sol.addStrings('123', '45'))
print(sol.addStrings('123', ''))
print(sol.addStrings('123', '0'))



