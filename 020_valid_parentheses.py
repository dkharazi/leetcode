"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

https://github.com/gengwg/leetcode
"""


class Solution(object):
    # use stack idea
    # http://www.cnblogs.com/zuoyuan/p/3779772.html
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for c in s:
            # push to stack when left parentheses
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            if c == ")":
                # if stack empty or not match pop, return false
                if stack == [] or stack.pop() != "(":
                    return False
            if c == "]":
                if stack == [] or stack.pop() != "[":
                    return False
            if c == "}":
                if stack == [] or stack.pop() != "{":
                    return False

        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    print Solution().isValid("([)]")
    print Solution().isValid("()")
    print Solution().isValid("()[]{}")