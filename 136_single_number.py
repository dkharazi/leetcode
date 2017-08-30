# -*- coding: utf-8 -*-
# 136. Single Number
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#

# The property of XOR.
# x ^ x = 0
# x ^ y ^ x = y (the order could in random arrangement)
# Since we have only one number appear once, other number appear perfectly twice.
# we XOR all numbers in the array, and we would finally get the number that only appears once.

import operator
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

    # use reduce
    def singleNumber(self, A):
        # function reduce(func, seq) continually applies the function func()
        # to the sequence seq. it returns a single value.

        return reduce(operator.xor, A)

    # use lambda
    def singleNumber(self, A):
        return reduce(lambda x, y: x ^ y, A)


if __name__ == "__main__":
    print Solution().singleNumber([1, 1, 2, 3, 2, 4, 3])
