# 290. Word Pattern

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.

# Examples:

#     pattern = "abba", str = "dog cat cat dog" should return true.
#     pattern = "abba", str = "dog cat cat fish" should return false.
#     pattern = "aaaa", str = "dog cat cat dog" should return false.
#     pattern = "abba", str = "dog dog dog dog" should return false.

# Notes:
# You may assume pattern contains only lowercase letters,
# and str contains lowercase letters separated by a single space.

class Solution(object):
    # map both list into numbers.
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern:
            return False

        a = [c for c in pattern]
        b = str.split()
        if len(a) != len(b):
            return False

        d1 = {}
        d2 = {}
        # d1 = d2 = {} will be wrong.

        i = 0
        for x in a:
            if x not in d1:
                d1[x] = i
                i += 1

        i = 0
        for x in b:
            if x not in d2:
                d2[x] = i
                i += 1

        for x, y in zip(a, b):
            if d1[x] != d2[y]:
                return False
        return True

    # use dict to record mapping on both directions
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern:
            return False
        a = [c for c in pattern]
        b = str.split()
        if len(a) != len(b):
            return False

        dic = dict(zip(a,b))
        dic2 = dict(zip(b,a))
        return [dic[x] for x in a] == b and [dic2[x] for x in b] == a

    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)
        # return map(s.index, s) == map(t.index, t)
        # py3
        # return list(map(s.find, s)) == list(map(t.index, t))

pattern = "abba"
str = "dog cat cat dog"
print(Solution().wordPattern(pattern, str))

pattern = "abba"
str = "dog cat cat fish"
print(Solution().wordPattern(pattern, str))
