"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

copyright:
    https://github.com/gengwg
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        lcp = ''

        # lcp can not be longer than min length among all the strings
        for i in range(len(min(strs, key=len))):
            # check if ith position is the same among all strings
            if all( strs[0][i] == s[i] for s in strs):
                # if so add it to lcp
                lcp += strs[0][i]
            else:
                # if not, stop immediately and return last remembered lcp.
                # no need check further
                return lcp

        return lcp


if __name__ == '__main__':
    print Solution().longestCommonPrefix(["aa", "ab"])
    print Solution().longestCommonPrefix([])
    print Solution().longestCommonPrefix(["aca", "cba"])