"""
49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

author: https://github.com/gengwg

use a dictionary.
the key is sorted string;
value is list of anagrams.

if sorted string == key, it is a anagram.
append it to the value list.

else create a new anagram list, with key as sorted string.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        d ={}
        for st in strs:
            key = ''.join(sorted(st))
            if key not in d:
                d[key] = [st]
            else:
                d[key].append(st)
        return d.values()

if __name__ == '__main__':
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])