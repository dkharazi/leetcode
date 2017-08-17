# -*- coding: utf-8 -*-
"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())",
where the longest valid parentheses substring is "()()", which has length = 4.

使用栈。这个解法比较巧妙，开辟一个栈，压栈的不是括号，而是未匹配左括号的索引！
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3780312.html
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        last = -1

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i - last)
                    else:
                        maxlen = max(maxlen, i - stack[len(stack) - 1])
        return maxlen

if __name__ == '__main__':
    print Solution().longestValidParentheses("(()")
    print Solution().longestValidParentheses(")()())")
