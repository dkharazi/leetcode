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
            if all(strs[0][i] == s[i] for s in strs):
                # if so add it to lcp
                lcp += strs[0][i]
            else:
                # if not, stop immediately and return last remembered lcp.
                # no need check further
                return lcp

        return lcp

    # use separate lcp function
    # https://gengwg.blogspot.com/2018/02/leoleetcode-14-longest-common-prefix.html
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            res = strs[0]
            for i in range(1, len(strs)):
                res = self.lcp(res, strs[i])
            return res

    def lcp(self, short, long):
        if len(short) > len(long):
            return self.lcp(long, short)
        else:
            for i in range(0, len(short)):
                if short[i] != long[i]:
                    return short[:i]
            return short

    # zip dafa
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        for index, value in enumerate(zip(*strs)):
            if len(set(value)) != 1:
                return strs[0][:index]
        return min(strs, key=len)


if __name__ == '__main__':
    print Solution().longestCommonPrefix(["aa", "ab"])
    print Solution().longestCommonPrefix([])
    print Solution().longestCommonPrefix(["aca", "cba"])
    print Solution().longestCommonPrefix(["c", "cba"])
