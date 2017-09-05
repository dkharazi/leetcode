# 171. Excel Sheet Column Number
#
# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i, c in enumerate(s[::-1]):
            res += (26 ** i) * (ord(c) - ord('A') + 1)
        return res

    # http://blog.csdn.net/coder_orz/article/details/51406455
    def titleToNumber(self, s):
        res = 0
        for c in s:
            res = res * 26 + ord(c) - ord('A') + 1
        return res


if __name__ == '__main__':
    assert Solution().titleToNumber("AB") == 28
