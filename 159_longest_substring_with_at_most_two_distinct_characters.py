# [LeetCode] 159. Longest Substring with At Most Two Distinct Characters

# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
# For example, Given s = “eceba” and k = 2,
# T is "ece" which its length is 3.


class Solution:
    # ref. 340
    # 思路:
    # 一个hash表和一个左边界标记.
    # 遍历字符串将其加入到hash表中,
    # 不同字符多于k个了, 就从左边开始删字符. 直到hash表不同字符长度等于k.
    # 此时字符串的长度就是当前字符和左边界的距离.
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        left = 0
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
            while len(d) > 2:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
            maxlen = max(maxlen, i-left+1)
        return maxlen

print (Solution().lengthOfLongestSubstringTwoDistinct('eceeba'))
print (Solution().lengthOfLongestSubstringTwoDistinct('eeeee'))
print (Solution().lengthOfLongestSubstringTwoDistinct('abcde'))
