"""
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        return len(s.split()[-1])

    # one liner
    def lengthOfLastWord(self, s):
        return len(s.split()[-1]) if s.split() != [] else 0


if __name__ == '__main__':
    print Solution().lengthOfLastWord("Hello World")
    print Solution().lengthOfLastWord("   ")
