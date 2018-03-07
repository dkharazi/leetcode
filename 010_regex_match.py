"""
10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true
"""


# https://gengwg.blogspot.com/2017/08/leetcode-10-regular-expression-matching.html
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        if p[-1] == '*':
            if s and (s[-1] == p[-2] or p[-2] == '.'):
                return self.isMatch(s, p[:-2]) or self.isMatch(s[:-1], p)
            else:
                return self.isMatch(s, p[:-2])
        else:
            if s and (s[-1] == p[-1] or p[-1] == '.'):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False


if __name__ == '__main__':
    print Solution().isMatch("aa", "a")
    print Solution().isMatch("aa", "aa")
    print Solution().isMatch("aaa", "aa")
    print Solution().isMatch("aa", "a*")
    print Solution().isMatch("aa", ".*")
    print Solution().isMatch("ab", ".*")
    print Solution().isMatch("aab", "c*a*b")
