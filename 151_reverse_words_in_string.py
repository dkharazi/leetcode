# 151. Reverse Words in a String
#
# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
class Solution:
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))

    # pythonic
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

if __name__ == "__main__":
    print Solution().reverseWords("the sky is blue")
