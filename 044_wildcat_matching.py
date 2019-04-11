# 44. Wildcard Matching
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    #
    # http://www.voidcn.com/article/p-hgfivloj-bhv.html
    def isMatch(self, s, p):
        i = 0
        j = 0
        sstar = 0
        star = -1
        while i < len(s):
            # compare ? or whether they are the same
            if j < len(p) and (s[i] == p[i] or p[j] == '?'):
                i += 1
                j += 1
            # if there is a * in p we mark current j and i
            elif j < len(p) and p[j] == '*':
                star = j
                j += 1
                sstar = i
            # if current p[j] is not * we check whether prior state has *
            elif star != -1:
                j = star + 1
                sstar += 1
                i = sstar
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1

        # return j == len(p)
        if j == len(p):
            return True
        return False

print(Solution().isMatch("ab", "?*"))
