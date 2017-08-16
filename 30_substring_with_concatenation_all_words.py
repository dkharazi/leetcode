"""
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words,
words, that are all of the same length.
Find all starting indices of substring(s) in s
that is a concatenation of each word in words exactly once
and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
import re
import itertools


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

    # TLE
    def findSubstring(self, s, words):
        res = []
        for t in itertools.permutations(words):
            pattern = '(?=({}))'.format("".join(t))
            res += [ m.start() for m in re.finditer(pattern, s) ]
            # this not work for overlapping matches
            # res += [m.start() for m in re.finditer(r'(?=("".join(t)))', s)]

        return list(set(res))


if __name__ == '__main__':
    print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])

    print Solution().findSubstring("aaa", ["a", "a"])