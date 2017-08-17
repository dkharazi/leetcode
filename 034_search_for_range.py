# -*- coding: utf-8 -*-
"""
34. Search for a Range

Given an array of integers sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

解题思路：又是二分查找的变形。
因为题目要求的时间复杂度是O(log n)。在二分查找到元素时，需要向前和向后遍历来找到target元素的起点和终点。


"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        found = []
        for i, num in enumerate(nums):
            if num == target:
                found.append(i)

        if not found:
            return [-1, -1]
        elif len(found) == 1:
            return [found[0], found[0]]
        else:
            return [found[0], found[-1]]
        
    # http://www.cnblogs.com/zuoyuan/p/3775904.html
    def searchRange(self, nums, target):
        left = 0; right = len(nums) -1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                list = [0, 0]
                if nums[left] == target:
                    list[0] = left
                if nums[right] == target:
                    list[1] = right
                for i in range(mid, right + 1):
                    if nums[i] != target:
                        list[1] = i - 1; break
                for i in range(mid, left - 1, -1):
                    if nums[i] != target:
                        list[0] = i + 1; break
                return list
        return [-1, -1]

if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
    print Solution().searchRange([4, 5], 5)
