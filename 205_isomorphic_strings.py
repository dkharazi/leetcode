# 205. Isomorphic Strings
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        dict = {}
        for x, y in zip(s, t):
            if x not in dict:
                dict[x] = y
            else:
                if dict[x] != y:
                    return False
        return True

    # http://blog.csdn.net/aliceyangxi1987/article/details/50300921
    def isIsomorphic(self, s, t):
        sdict = {}
        tdict = {}
        for i, j in zip(s, t):
            if i not in sdict:
                sdict[i] = j
            if j not in tdict:
                tdict[j] = i
            if sdict[i] != j or tdict[j] != i:
                return False
        return True

    # http://blog.csdn.net/coder_orz/article/details/51681396
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


if __name__ == '__main__':
    print Solution().isIsomorphic("egg", "add")
    print Solution().isIsomorphic("foo", "bar")
    print Solution().isIsomorphic("paper", "title")
    print Solution().isIsomorphic("ab", "aa")
