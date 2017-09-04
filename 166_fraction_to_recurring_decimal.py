# -*- coding: utf-8 -*-
# 166. Fraction to Recurring Decimal
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
#
# Credits:
# Special thanks to @Shangrila for adding this problem and creating all test cases.
#
#
# https://shenjie1993.gitbooks.io/leetcode-python/166%20Fraction%20to%20Recurring%20Decimal.html
# 能够除尽的很简单，就是模拟一个除法操作，
# 对于无限循环小数，如果哪一次的余数在之前已经出现过了，那么继续算下去就会出现循环，
# 这时候就可以停止运算，并将这两位之间的数添加到括号中。
# 整数部分不存在循环问题，所以可以先单独计算，符号也可以先确定。
# 因为是判断是否有重复的余数，对于能够除尽的情况，重复的余数是除尽后的0，
# 所以末尾会多个"(0)"，要去掉。
# 而能够整除的情况，要把小数点也去掉。


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        result_list = [sign, str(quotient), '.']
        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            result_list.append(str(quotient))

        idx = remainders.index(remainder)
        # insert ( after .
        # includes sign at the front..
        # [sign, number before '.', '.'] == 3 elements
        result_list.insert(idx + 3, '(')
        result_list.append(')')
        result = ''.join(result_list).replace('(0)', '').rstrip('.')
        return result


if __name__ == '__main__':
    print Solution().fractionToDecimal(1, 6)
    print Solution().fractionToDecimal(2, 3)
