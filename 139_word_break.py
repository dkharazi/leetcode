# 139. Word Break
#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        http://www.cnblogs.com/zuoyuan/p/3760660.html
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True

        return dp[len(s)]


if __name__ == '__main__':
    print Solution().wordBreak("leetcode", ["leet", "code"])
    print Solution().wordBreak("cars", ["car", "ca", "rs"])
