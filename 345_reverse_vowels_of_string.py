# 345. Reverse Vowels of a String

# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y". 

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = []
        indices = []
        res = []
        for i, ch in enumerate(s):
            if ch in v:
                vowels.append(ch)
                indices.append(i)
            else:
                res.append(ch)
        vowels.reverse()
        for (i, x) in zip(indices, vowels):
            res.insert(i, x)
        return ''.join(res)

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        s1 = list(s)
        for i in range(len(vowels)//2):
            s1[vowels[i]], s1[vowels[-i-1]] = s1[vowels[-i-1]], s1[vowels[i]]
        return ''.join(s1)
