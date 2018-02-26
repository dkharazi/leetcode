"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        author: http://www.cnblogs.com/zuoyuan/p/3777721.html
        :type s: str
        :rtype: str
        """
        palindrome = ''
        # at every position, check the longest palin here
        for i in range(len(s)):
            # odd palindrome case, e.g. "aba"
            len1 = len(self.getlongestpalindrome(s, i, i))
            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i)

            # even palindrome case, e.g. "abba"
            len2 = len(self.getlongestpalindrome(s, i, i + 1))
            if len2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i + 1)
        return palindrome

    # check longest palin at position i
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        # l, r now out of range (0, len(s)-1)
        return s[l + 1: r]

    # TLE
    def longestPalindromeBrutal(self, s):
        """
        1. get all substrings
        2. check if a palin, if so put in a palin set
        3. return the longest palin out of the palin set
        :param s: str
        :return: str
        """

        results = set()
        for i in range(len(s) + 1):
            for j in range(0, i):
                chunk = s[j:i + 1]
                if chunk == chunk[::-1]:
                    results.add(chunk)
        return max(results, key=len)

    def isPalindrome(self, st):
        return st == st[::-1]


if __name__ == '__main__':
    print Solution().longestPalindrome("babad")
    print Solution().longestPalindrome("cbbd")
    print Solution().longestPalindrome("c")
