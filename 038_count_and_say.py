"""
38. Count and Say

The count-and-say sequence is the sequence of integers
with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3781329.html

    def count(self, s):
        t = ''; count = 0; curr = '#'
        for c in s:
            if c != curr:
                if curr != '#':
                    t += str(count) + curr
                curr = c
                count = 1
            else:
                count += 1

        # now either curr = last c; count = 1.
        # or curr = last c; count = N (N > 1)
        # either way, when the for loop exits
        # curr and count are not concanated
        t += str(count) + curr
        return t

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(2, n + 1):
            s = self.count(s)
        return s

if __name__ == '__main__':
    print Solution().countAndSay(6)