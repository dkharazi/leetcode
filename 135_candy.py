# -*- coding: utf-8 -*-
# 135. Candy
#
# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
# What is the minimum candies you must give?


class Solution(object):
    def candy(self, ratings):
        """
        https://shenjie1993.gitbooks.io/leetcode-python/135%20Candy.html
        从前往后遍历的时候，我们只考虑升序的序列，
        对于其中一段升序的序列，最理想的情况是按照1,2,3...这样分发糖果；
        而对于降序的序列，如果从后往前遍历就也变成升序的了。
        通过前序和后序遍历后，升序与降序的交接处那个点会有两个值，
        因为要比两边的孩子拿到的糖果都多，所以取较大的那个值。
        这时候得到的数组就是在满足题目要求前提下每个孩子拿到的最少的糖果数，返回它的和即可。
\
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        # each child has at least one candy
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


if __name__ == "__main__":
    assert Solution().candy([1, 2, 3, 2]) == 7
    assert Solution().candy([1, 2, 3, 7, 4, 3, 2, 1]) == 21
