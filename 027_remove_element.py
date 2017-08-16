"""
27. Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

https://github.com/gengwg/leetcode
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.remove(val)

        return len(nums)

    # http://www.cnblogs.com/zuoyuan/p/3779848.html
    def removeElement(self, nums, val):

        # move from right side!
        j = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                # move all val elements to the end
                nums[i], nums[j] = nums[j], nums[i]
                # advance j
                j -= 1
        # j now points to last non val element
        return j + 1


if __name__ == '__main__':
    print Solution().removeElement(nums = [3, 2, 2, 3], val = 3)
    print Solution().removeElement(nums = [2, 2], val = 3)