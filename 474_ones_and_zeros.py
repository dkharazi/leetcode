# 474. Ones and Zeroes

# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
#
# For now, suppose you are a dominator of m 0s and n 1s respectively.
# On the other hand, there is an array with strings consisting of only 0s and 1s.
#
# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s.
# Each 0 and 1 can be used at most once.
#
# Note:
#
#     The given numbers of 0s and 1s will both not exceed 100
#     The size of given string array won't exceed 600.
#
# Example 1:
#
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
#
# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
#
# Example 2:
#
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
#
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

# https://leetcode.com/problems/ones-and-zeroes/discuss/95814/c++-DP-solution-with-comments

class Solution(object):
    # https://blog.csdn.net/fuxuemingzhu/article/details/82825032
    # 看到这个题第一个感觉是贪心，但是想了想，
    # 无论是贪心少的还是贪心多的，都会影响到后面选取的变化，所以不行。
    # 遇到这种求最多或最少的次数的，并且不用求具体的解决方案，一般都是使用DP。

    # 这个DP很明白了，定义一个数组dp[m+1][n+1]，代表m个0, n个1能组成的最长字符串。
    # 遍历每个字符串统计出现的0和1得到zeros和ones，
    # 所以第dp[i][j]的位置等于dp[i][j]和dp[i - zeros][j - ones] + 1。
    # 其中dp[i - zeros][j - ones]表示如果取了当前的这个字符串，那么剩下的可以取的最多的数字。

    # 时间复杂度有点难计算，大致是O(MN * L), L 是数组长度，空间复杂度是O(MN).
    # TLE
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zeros, ones = 0, 0
            # count zeros and ones
            for c in s:
                if c == '0':
                    zeros += 1
                elif c == '1':
                    ones += 1
		# dp[i][j] = the max number of strings that can be formed with i 0's and j 1's
		# from the first few strings up to the current string s
		# Catch: have to go from bottom right to top left
		# Why? If a cell in dp is updated (because s is selected),
		# we should be adding 1 to dp[i][j] from the previous iteration (when we were not considering s)
		# If we go from top left to bottom right, we would be using results from this iteration => overcounting
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[m][n]

print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
print(Solution().findMaxForm(["10", "0", "1"], 1, 1))
