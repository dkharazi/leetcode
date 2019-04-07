# 161 One Edit Distance

# An edit between two strings is one of the following changes:
#
#     Add a character
#     Delete a character
#     Change a character
#
# Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit.
# Expected time complexity is O(m+n) where m and n are lengths of two strings.


class Solution:

    def isEditDistanceOne(self, s1, s2):
        n = len(s1)
        m = len(s2)
        if n == m:
            return self.__isChangeOne(s1, s2, n)
        elif n == m - 1:
            return self.__isAddOne(s1, s2, n)
        elif n - 1 == m:
            return self.__isAddOne(s2, s1, m)
        else:
            return False

    def __isChangeOne(self, s1, s2, n):
        changed = False
        for i in range(n):
            if s1[i] != s2[i]:
                if changed:
                    return False
                changed = True
        return changed

    def __isAddOne(self, s1, s2, n):
        add = 0
        i = 0
        # for i in range(n):
        # https://jianlu.github.io/2016/11/09/leetcode161-One-Eidt-Distance/
        # above solution has bug. missed checking character immediately after diff
        # use while loop to fix it; retreat i when diff
        while i < n:
            if s1[i] != s2[i + add]:
                if add == 1:
                    return False
                add = 1
                i -= 1
            i += 1
        return add == 1


if __name__ == "__main__":
    sol = Solution()
    s1 = "gfg"
    s2 = "axag"
    print(sol.isEditDistanceOne(s1, s2))
    print(sol.isEditDistanceOne('abc', 'agbc'))
    print(sol.isEditDistanceOne('abc', 'agxc')) # test case for bug

