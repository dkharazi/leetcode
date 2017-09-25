# -*- coding: utf-8 -*-
# 214. Shortest Palindrome
#
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
# Find and return the shortest palindrome you can find by performing this transformation.
#
# For example:
#
# Given "aacecaaa", return "aaacecaaa".
#
# Given "abcd", return "dcbabcd".
#
# http://bookshadow.com/weblog/2015/05/22/leetcode-shortest-palindrome/
# 解题思路：
#
# KMP算法
# https://zh.wikipedia.org/wiki/%E5%85%8B%E5%8A%AA%E6%96%AF-%E8%8E%AB%E9%87%8C%E6%96%AF-%E6%99%AE%E6%8B%89%E7%89%B9%E7%AE%97%E6%B3%95
#
# 参考LeetCode Discuss链接：https://leetcode.com/discuss/36807/c-8-ms-kmp-based-o-n-time-%26-o-n-memory-solution
#
# 记原始字符串为s，s的反转字符串为rev_s。
#
# 构造字符串l = s + '#' + rev_s，其中'#'为s中不会出现的字符，添加'#'是为了处理输入为空字符串的情形。
#
# 对字符串l执行KMP算法，可以得到“部分匹配数组”p（也称“失败函数”）
#
# 我们只关心p数组的最后一个值p[-1]，因为它表明了rev_s与s相互匹配的最大前缀长度。
#
# 最后只需要将rev_s的前k个字符与原始串s拼接即可，其中k是s的长度len(s)与p[-1]之差。


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s = s[::-1]
        l = s + '#' + rev_s
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        # print p
        return rev_s[: len(s) - p[-1]] + s


if __name__ == '__main__':
    print Solution().shortestPalindrome("abcd")
    print Solution().shortestPalindrome("abab")
    print Solution().shortestPalindrome("aacecaaa")
