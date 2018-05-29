# 279. Perfect Squares

# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
# given n = 13, return 2 because 13 = 4 + 9.

class Solution(object):
    # https://gengwg.blogspot.com/2018/02/leetcode-279-perfect-squares.html
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import sys
        # dp[n] indicates that the perfect squares count of the given n
        dp = [sys.maxint] * (n+1)
        # dp = [n] * (n+1)
        # dp[0] is 0. thus also n+1 array size.
        dp[0] = 0
        # calculate dp[1] to dp[n]
        for i in range(1, n+1):
            j = 1
            # To get the value of dp[n], we should choose the min
            # value from:
            #     dp[n - 1] + 1,
            #     dp[n - 4] + 1,
            #     dp[n - 9] + 1,
            #     dp[n - 16] + 1
            #     and so on...
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]

    # https://www.jiuzhang.com/solution/perfect-squares/#tag-highlight-lang-python
    def numSquares(self, n):
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        for i in xrange(n+1):
            temp = i * i
            if temp <= n:
                if int((n - temp)** 0.5 ) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3

print Solution().numSquares(12)
print Solution().numSquares(13)
print Solution().numSquares(6993)
