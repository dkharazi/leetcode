# -*- coding: utf-8 -*-
"""
35. Search Insert Position

Given a sorted array and a target value,
return the index if the target is found.
If not, return the index where it would be
if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

https://github.com/gengwg
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) / 2 + l
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else: # target > nums[mid]
                l = mid + 1

        # print l, r
        return l

        # l = r + 1
        """
        if target > nums[r]:
            return r + 1

        if target < nums[l]:
            return l
        """


if __name__ == '__main__':
    print Solution().searchInsert([1, 3, 5, 6], 5)
    print Solution().searchInsert([1, 3, 5, 6], 2)
    print Solution().searchInsert([1, 3, 5, 6], 7)
    print Solution().searchInsert([1, 3, 5, 6], 0)