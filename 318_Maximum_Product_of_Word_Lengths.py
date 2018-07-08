# 318. Maximum Product of Word Lengths

# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
# where the two words do not share common letters. 
# You may assume that each word will contain only lower case letters. 
# If no such two words exist, return 0.

# Example 1:

# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".

# Example 2:

# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".

# Example 3:

# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.


class Solution(object):
    # https://www.hrwhisper.me/leetcode-maximum-product-of-word-lengths/

    # nums[i] |= 1 << (c - 'a') is using bit to represent if a char exists in the word.
    # For example, if a and b exists, it will be 11 (binary).

    # if((nums[i] & nums[j]) == 0 is to check if the two words have common chars.

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        elements = [0] * n
        for i, s in enumerate(words):
            for c in s:
                elements[i] |= 1 << (ord(c) - 97)

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (elements[i] & elements[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

s = Solution()
print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))

