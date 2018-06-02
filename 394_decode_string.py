# 394. Decode String

# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string], 
# where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; 
# No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits 
# and that digits are only for those repeat numbers, k. 
# For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution(object):
    # stack
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curStr = ''
        for c in s:
            if c == '[':
                # push current string and number got so far
                stack.append(curStr)
                stack.append(curNum)
                # reset to empty/zero
                curStr = ''
                curNum = 0
            elif c == ']':
                # pop num and previous string
                num = stack.pop()
                prevStr = stack.pop()
                # add prev string to cur * n
                curStr = prevStr + num * curStr
            elif c.isdigit():
                # in case of '32[a]'
                curNum = curNum * 10 + int(c)
            else:
                curStr += c
        return curStr

    #  regular expression
    def decodeString(self, s):
        import re
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s

if __name__ == '__main__':
    s = "2[abc]3[cd]ef"
    print(Solution().decodeString(s))