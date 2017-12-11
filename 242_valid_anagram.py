# 242. Valid Anagram
#
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
#     You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#
# http://blog.csdn.net/coder_orz/article/details/51406015



class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}

        for c in s:
            if c in ds:
                ds[c] += 1
            else:
                ds[c] = 1

        for c in t:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1

        return ds == dt

    def isAnagram(self, s, t):
        if len(s) ! = len(t):
            return False
        alpha = {}
        beta = {}
        for c in s:
            alpha[c] = alpha.get(c, 0) + 1
        for c in t:
            beta[c] = beta.get(c, 0) + 1
        return alpha == beta

    # sort and compare if they are equal
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

s = "rat"
t = "car"
print Solution().isAnagram(s, t)
