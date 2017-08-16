"""
28. Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

https://github.com/gengwg
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0

        # need compare lenA-lenB+1 times!
        for i in range(len(haystack) - len(needle) + 1):
            # at every position i, compare haystack[i:i+len+1] with needle[0:len+1]
            if all([(haystack[x] == needle[y])
                    for (x, y) in
                    zip(range(i, i + len(needle)), range(len(needle)))]):
                # return first match
                return i

        return -1

        # return haystack.index(needle)

if __name__ == '__main__':
    print Solution().strStr("aabc", "ab")   # 1
    print Solution().strStr("aa", "aa")     # 0