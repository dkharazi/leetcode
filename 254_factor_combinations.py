# 254 Factor Combinations

# Numbers can be regarded as product of its factors. For example,
#
# 8 = 2 x 2 x 2;
#   = 2 x 4.
#
# Write a function that takes an integer n and return all possible combinations of its factors.
#
# Note:
#
#     You may assume that n is always positive.
#     Factors should be greater than 1 and less than n.
#
# Examples:
# input: 1
# output:
#
# []
#
# input: 37
# output:
#
# []
#
# input: 12
# output:
#
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
#
# input: 32
# output:
#
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
#

import math

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 1:
            return []
        res = []
        self.helper(n, 2, [], res)
        return res

    # dfs
    # https://nb4799.neu.edu/wordpress/?p=2416
    # target: the remaining factors should multiply to target
    # start_num: the remaining factors should be equal to or larger than start_num
    # factors: the factors so far, stored in a list
    def helper(self, target, start_num, factors, res):
        # if factors:
        #     res.append(factors + [target])
        if target == 1:
            if len(factors) > 1:
                res.append(list(factors))
                return

        #for i in range(start_num, int(math.sqrt(target))+1):
        for i in range(start_num, target+1):
            if target % i == 0:
                factors.append(i)
                self.helper(target//i, i, factors, res)
                factors.pop()

sol = Solution()
print(sol.getFactors(8))
print(sol.getFactors(12))
print(sol.getFactors(32))
