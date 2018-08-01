# 249. Group Shifted Strings

# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"

# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# A solution is:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
#

from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        d = defaultdict(list)
        for s in strings:
            code = self.encode(s)
            d[code].append(s)
        return d.values()

    def encode(self, s):
        res = ''
        for i in range(1, len(s)):
            tmp = (ord(s[i]) - ord(s[i-1]) + 26) % 26
            res += chr(tmp)
        return res

sol = Solution()
print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
