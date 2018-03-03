# -*- coding: utf-8 -*-
# 121. Best Time to Buy and Sell Stock
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.


class Solution(object):
    # brutal
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        maxp = 0
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > maxp:
                    maxp = prices[j] - prices[i]
        return maxp

    # http://www.cnblogs.com/zuoyuan/p/3765934.html
    # 解题思路：扫描一遍数组，使用low来标记最低价位，如果有更低的价位，置换掉。
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0

        low = prices[0]
        maxprofit = 0
        for i in range(n):
            if prices[i] < low:
                low = prices[i]
            if prices[i] - low > maxprofit:
                maxprofit = prices[i] - low
        return maxprofit

    # enumerate dafa
    # record both min price and max profit
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxprofit = 0
        minprice = prices[0]
        for index, price in enumerate(prices):
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price-minprice)
        return maxprofit


if __name__ == '__main__':
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
