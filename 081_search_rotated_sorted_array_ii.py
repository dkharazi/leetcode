# -*- coding: utf-8 -*-
"""
81. Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.


http://blog.csdn.net/aliceyangxi1987/article/details/50560697

有重复的话，多了一个判断条件就是三点相等时，左右端点同时变化

影响就是，如果在重复中间截断逆转，
之后再用 nums[start]<=target<nums[mid] 去判断，就找不到这个target
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[start] == nums[end]:
                start += 1
                end -= 1
            elif nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False


if __name__ == '__main__':
    print Solution().search([3, 1, 1, 2], 2)
