"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

  Given "abcabcbb", the answer is "abc", which the length is 3.

  Given "bbbbb", the answer is "b", with the length of 1.

  Given "pwwkew", the answer is "wke", with the length of 3.
  Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstringBrutal(self, s):
        """
        :type s: str
        :rtype: int
        """
        # brutal force solution

        if len(s) < 2:
            return len(s)

        res = []
        for i in range(0, len(s) - 1):
            # record longest length starting from this position
            longest = 1
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    break
                longest += 1
            res.append(longest)

        #print res
        return max(res)

    # sliding window
    # author: http://www.cnblogs.com/zuoyuan/p/3785840.html
    def lengthOfLongestSubstring(self, s):
        start = 0;
        maxlen = 0;
        dict = {}

        for i in range(len(s)): dict[s[i]] = -1

        for end in range(len(s)):
            # as soon as there is duplicate
            # record the current max distance if larger than previous one
            # and advance start to duplicate position + 1
            # because anything between is shorter than current substring
            if dict[s[end]] != -1:
                while start <= dict[s[end]]:
                    # remove below line, and end result is the same
                    # because if start > dict[s[end]],
                    # it just will not advance, and keep the original value
                    dict[s[start]] = -1
                    start += 1
                # this is not equivalent!!
                # it will change the value backward
                # start = dict[s[end]] + 1

            # print start, dict[s[end]], end

            if end - start + 1 > maxlen:
                maxlen = end - start + 1

            dict[s[end]] = end
            # print dict

        return maxlen

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("abba")
    print Solution().lengthOfLongestSubstring("dvdf")
    print Solution().lengthOfLongestSubstring("pwwkew")
