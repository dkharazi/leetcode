# -*- coding: utf-8 -*-
"""
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.

http://www.cnblogs.com/zuoyuan/p/3783453.html

解题思路：一种巧妙的解法。
使用两个指针prev和curr，
判断A[curr]是否和A[prev]、A[prev-1]相等，
如果相等curr指针继续向后遍历，
直到不相等时，将curr指针指向的值赋值给A[prev+1]，
这样多余的数就都被交换到后面去了。
最后prev+1值就是数组的长度。

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)

        prev = 1;
        curr = 2
        while curr < len(nums):
            if nums[curr] == nums[prev] and nums[curr] == nums[prev - 1]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        return prev + 1


if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
