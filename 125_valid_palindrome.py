# 125. Valid Palindrome
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s.lower() if e.isalnum())
        return s == s[::-1]

    # http://blog.csdn.net/aliceyangxi1987/article/details/50372724
    # not use isalnum()
    def isPalindrome(self, s):
        new = []
        for e in s.lower():
            if '0' <= e < '9' or 'a' <= e <= 'z':
                new.append(e)

        return new == new[::-1]

    # not use s[::-1]
    def isPalindrome(self, s):
        s = ''.join(e for e in s.lower() if e.isalnum())
        for i in range(0, len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    assert Solution().isPalindrome("race a car") is False
