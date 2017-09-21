# -*- coding: utf-8 -*-
# 213. House Robber II
# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place for his thievery
# so that he will not get too much attention. This time, all houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# http://bookshadow.com/weblog/2015/05/20/leetcode-house-robber-ii/
#
# 讨论是否抢劫第一件房屋。如果是，则不可以抢最后一件房屋。否则，可以抢最后一间房屋。
#
# 以此为依据，将环形DP问题转化为两趟线性DP问题，可以复用House Robber的代码。
#
# 另外需要特判一下只有一件房屋的情形。


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))

    def robLinear(self, nums):
        dp = [0] * len(nums)
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    print Solution().rob([1, 2, 2, 1])
