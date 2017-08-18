# -*- coding: utf-8 -*-
"""
41. First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):
    # https://www.hrwhisper.me/leetcode-first-missing-positive/
    # 思路，将值为x的数放在下标x-1的位置，
    # 即：A[i]存放的应该是i+1这个数。
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i, n = 0, len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # A[i], A[A[i] - 1]  = A[A[i] - 1] , A[i] error!
            else:
                i += 1

        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

    # http://www.cnblogs.com/zuoyuan/p/3777496.html
    def firstMissingPositive(self, nums):

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 2
        for i in range(n):
            if abs(nums[i]) <= n:
                curr = abs(nums[i]) - 1
                nums[curr] = -abs(nums[curr])
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

    def test(self, nums):
        if not nums:
           return 1
        for x in nums:
            if x < 0:
                nums.remove(x)
        n = max(nums)
        return n * (n  + 1) / 2 - sum(nums) or n + 1

if __name__ == '__main__':
    print Solution().firstMissingPositive([1, 3, -1, 4])
    print Solution().firstMissingPositive([1, 2, 0])
    print Solution().firstMissingPositive([0])
