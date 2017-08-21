# -*- coding: utf-8 -*-
"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

author: gengwg

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # pad smaller one with leading 0s
        pad = abs(len(a) - len(b))
        small = a if len(a) < len(b) else b
        big = a if len(a) >= len(b) else b
        small = '0' * pad + small
        # print big, small

        res = []
        carry = 0
        for i in range(len(big) - 1, -1, -1):
            digit = (int(big[i]) + int(small[i]) + carry) % 2
            carry = (int(big[i]) + int(small[i]) + carry) / 2
            res.insert(0, digit)  # insert digit at the beginning

        if carry:
            res = [1] + res
        return ''.join(str(d) for d in res)

    # http://blog.csdn.net/coder_orz/article/details/51706532
    # 从两个字符串的最低位开始，
    # 一位一位的进行二进制相加，并保存进位，
    # 最终可以得到两者的和的字符串。
    def addBinary(self, a, b):
        res = ''
        i, j, plus = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or plus == 1:
            plus += int(a[i]) if i >= 0 else 0
            plus += int(b[j]) if j >= 0 else 0
            res = str(plus % 2) + res
            i, j, plus = i - 1, j - 1, plus / 2
        return res


if __name__ == '__main__':
    print Solution().addBinary('11', '1')
    print Solution().addBinary('101', '101')
    print Solution().addBinary('1', '0')
