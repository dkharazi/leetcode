# -*- coding: utf-8 -*-
# 132. Palindrome Partitioning II
#
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s) + 1)]
        p = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) + 1):
            dp[i] = len(s) - i
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j - i) < 2) or p[i + 1][j - 1]):
                    p[i][j] = True
                    dp[i] = min(1 + dp[j + 1], dp[i])

        return dp[0] - 1

    # https://shenjie1993.gitbooks.io/leetcode-python/132%20Palindrome%20Partitioning%20II.html
    # 可以通过动态规划解决，
    # dp[i]表示字符串s[:i+1]需要的最少的切割次数，
    # dp[i]的初始值为i，因为长度为i+1的字符串最多切割i次就能满足题目要求 。
    # 当添加一个字符后，我们需要依次判断以它为末尾的子字符串是否是回文字符串，
    # 如果是，则要计算剩余字符串需要的最少切割次数加上一次是否能使当前的最少切割次数更少，
    # 注意如果此时整个字符串就是回文字符串，则最少切割次数为0。
    # 递推表达式如下：
    # dp[i] = 0, 如果s[:i+1]是回文串
    # dp[i] = min(dp[i], dp[j-1]+1), 如果s[j:i+1]是回文串
    # 为了减少判断回文字符串时的计算，我们通过一个二维数组isPal[j][i]来缓存判断结果，
    # isPal[j][i]表示字符串s[j:i+1]是否是回文字符串。

    def minCut(self, s):
        n = len(s)
        dp = [0 for _ in range(n)]
        isPal = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            m = i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
                    m = 0 if j == 0 else min(m, dp[j - 1] + 1)
            dp[i] = m
        return dp[-1]


if __name__ == '__main__':
    print Solution().minCut("aab")
