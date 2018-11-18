# 266. Palindrome Permutation
#
# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
#
# Example 2:
#
# Input: "aab"
# Output: true
#
# Example 3:
#
# Input: "carerac"
# Output: true

# https://leetcode.com/articles/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        unpaired_chars = set()

        for c in s:
            if c not in unpaired_chars:
                unpaired_chars.add(c)
            else:
                unpaired_chars.remove(c)

        return len(unpaired_chars) <= 1

