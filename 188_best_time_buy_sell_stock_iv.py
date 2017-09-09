# -*- coding: utf-8 -*-
# 188. Best Time to Buy and Sell Stock IV
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.


class Solution(object):
    def maxProfit(self, k, prices):
        """
        http://bookshadow.com/weblog/2015/02/18/leetcode-best-time-to-buy-and-sell-stock-iv/
        动态规划（Dynamic Programming）

        问题的实质是从长度为n的prices数组中挑选出至多2 * k个元素，组成一个交易（买卖）序列。

        交易序列中的首次交易为买入，其后卖出和买入操作交替进行。

        总收益为交易序列中的偶数项之和 - 奇数项之和。
        dp[j]表示完成j次交易时的最大收益，转移方程如下：

        dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])

        当j为奇数时，交易类型为买入；

        当j为偶数时，交易类型为卖出。
        由于直接采用动态规划会返回Time Limit Exceeded，可以针对题目部分样例做出下面的优化：

        令最大交易次数为k，数组长度为size；

        则当k > size / 2时，问题可以转化为：Best Time to Buy and Sell Stock II
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if k > size / 2:
            return self.quickSolve(size, prices)

        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in range(size):
            for j in range(min(2 * k, i + 1), 0, - 1):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        return max(dp)

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]

        return sum


if __name__ == '__main__':
    print Solution().maxProfit(1, [7, 1, 5, 3, 6, 4])
    print Solution().maxProfit(2, [7, 6, 4, 3, 1])
