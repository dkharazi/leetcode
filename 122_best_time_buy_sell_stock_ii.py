# -*- coding: utf-8 -*-
# 122. Best Time to Buy and Sell Stock II
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        http://www.cnblogs.com/zuoyuan/p/3765980.html
        解题思路：由于可以进行无限次的交易，那么只要是递增序列，就可以进行利润的累加。

        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit


if __name__ == '__main__':
    print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 6, 4, 3, 1])
