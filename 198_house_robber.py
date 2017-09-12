# -*- coding: utf-8 -*-
# 198. House Robber
#
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.


class Solution(object):
    # http://www.tangjikai.com/algorithms/leetcode-198-house-robber
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n + 1)
        if n > 0:
            dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[n]

    # http://blog.csdn.net/coder_orz/article/details/51555813
    # 这个问题可以这么想，假设只有一家，那么你只能偷这家；假设有两家，那么你要判断两家哪个钱多，偷哪个；
    # 依次类推，假设有n家，那么你要判断“偷第n家不偷第n-1家且前n-2家尽量多的偷”和“不偷第n家且前n-1家尽量多的偷”，哪个得到的钱多偷哪个。
    # 你可以递归求解，然而复杂度太高无法AC。所以应该记录已经计算过的结果，于是这变成一个动态规划问题。
    # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    def rob(self, nums):
        n = len(nums)
        dp = [0] * n
        if not nums:
            return 0
        elif n == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == '__main__':
    print Solution().rob([1, 2, 1])
