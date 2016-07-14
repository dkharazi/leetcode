# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
class Solution:
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))

if __name__ == "__main__":
    print Solution().reverseWords("the sky is blue.")
