# -*- coding: utf-8 -*-
# 123. Best Time to Buy and Sell Stock III
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
#


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        f1 = [0 for _ in range(length)]
        f2 = [0 for _ in range(length)]

        minV = prices[0]
        f1[0] = 0
        for i in range(1, length):
            minV = min(minV, prices[i])
            f1[i] = max(f1[i - 1], prices[i] - minV)

        maxV = prices[length - 1]
        f2[length - 1] = 0
        for i in range(length - 2, -1, -1):
            maxV = max(maxV, prices[i])
            f2[i] = max(f2[i + 1], maxV - prices[i])

        res = 0
        for i in range(length):
            if f1[i] + f2[i] > res:
                res = f1[i] + f2[i]
        return res

if __name__ == '__main__':
    print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 6, 4, 3, 1])
