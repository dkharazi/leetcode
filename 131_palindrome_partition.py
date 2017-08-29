"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

http://www.cnblogs.com/zuoyuan/p/3758437.html
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.res = []
        self.dfs(s, [])
        return Solution.res

    def isPalindrome(self, s):
        for i in range(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def dfs(self, s, stringlist):
        if len(s) == 0:
            Solution.res.append(stringlist)
        for i in range(1, len(s)):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist + [s[:i]])


if __name__ == "__main__":
    print Solution().partition("aab")
    print Solution().partition("abc")

