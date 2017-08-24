"""
76. Minimum Window Substring

Given a string S and a string T,
find the minimum window in S
which will contain all the characters in T
in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T,
return the empty string "".

If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.

"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        count1 = {}
        count2 = {}
        for char in t:
            if char not in count1:
                count1[char] = 1
            else:
                count1[char] += 1
        for char in t:
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1

        count = len(t)
        start = 0
        minSize = 100000
        minStart = 0
        for end in range(len(s)):
            if s[end] in count2 and count2[s[end]] > 0:
                count1[s[end]] -= 1
                if count1[s[end]] >= 0:
                    count -= 1
            if count == 0:
                while True:
                    if s[start] in count2 and count2[s[start]] > 0:
                        if count1[s[start]] < 0:
                            count1[s[start]] += 1
                        else:
                            break
                    start += 1
                if minSize > end - start + 1:
                    minSize = end - start + 1
                    minStart = start
        if minSize == 100000:
            return ''
        else:
            return s[minStart:minStart + minSize]


if __name__ == '__main__':
    print Solution().minWindow("ADOBECODEBANC", "ABC")
