# -*- coding: utf-8 -*-
# 179. Largest Number
# Given a list of non negative integers,
# arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large,
# so you need to return a string instead of an integer.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
# http://bookshadow.com/weblog/2015/01/13/leetcode-largest-number/
# 排序思路：
# 对于两个备选数字a和b，
# 如果str(a) + str(b) > str(b) + str(a)，
# 则a在b之前，否则b在a之前
#
# 按照此原则对原数组从大到小排序即可
#
# 时间复杂度O（nlogn）
#
# 易错样例：
# Input:     [0,0]
# Output:    "00"
# Expected:  "0"


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted([str(x) for x in nums], cmp=self.compare)
        ans = ''.join(nums).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        # 2nd [] is not a list. it is indexing: True = 1, False = 0
        # [1, -1][1] == -1; [1, -1][1] == 1
        # so this will sort a, b in reverted (descending) order
        return [1, -1][a + b > b + a]


if __name__ == '__main__':
    print Solution().largestNumber([3, 30, 34, 5, 9])
