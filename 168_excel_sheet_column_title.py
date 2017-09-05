# -*- coding: utf-8 -*-
# 168. Excel Sheet Column Title
#
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.
#
# http://blog.csdn.net/coder_orz/article/details/51406627
#
# 首先，我们要知道Excel里这个对应关系是什么样的。
# 从A-Z对应1-26，当列标题进一位变成AA时，列对应的数字变成27。
# 所以这个题本质上是一个10进制转26进制的问题，不过A对应的是1而不是0，要注意。
#
# 用处理进制转换的一般思路，重复取模和除法即可。
# 但是注意由于A对应1，所以Z之后是AA，这个转换不同于一般的进制转换。


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            res += chr(ord('A') + (n - 1) % 26)
            n = (n - 1) / 26
        return res[::-1]

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            # 'A' + 'B' = 'AB'
            # ==> put later results (msd) in front
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) / 26
        return res

    # recursion
    def convertToTitle(self, n):
        if n == 0:
            return ''
        return self.convertToTitle((n - 1) / 26) + chr(ord('A') + (n - 1) % 26)


if __name__ == '__main__':
    print Solution().convertToTitle(28)
