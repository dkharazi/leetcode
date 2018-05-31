# [LeetCode] 340. Longest Substring with At Most K Distinct Characters

# Given a string, find the length of the longest substring T that contains at most k distinct characters.
# For example, Given s = “eceba” and k = 2,
# T is "ece" which its length is 3.

class Solution:
    # https://blog.csdn.net/qq508618087/article/details/51049767
    # 思路:
    # 一个hash表和一个左边界标记.
    # 遍历字符串将其加入到hash表中,
    # 不同字符多于k个了, 就从左边开始删字符. 直到hash表不同字符长度等于k.
    # 此时字符串的长度就是当前字符和左边界的距离.
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxlen = 0
        left = 0
        dict = {}
        for i, c in enumerate(s):
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
            while len(dict) > k:
                dict[s[left]] -= 1
                if dict[s[left]] == 0:
                    del dict[s[left]]
                    left += 1
            maxlen = max(maxlen, i - left + 1)
        return maxlen

print (Solution().lengthOfLongestSubstringKDistinct('eceba', 2))





