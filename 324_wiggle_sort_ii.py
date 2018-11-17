# 324. Wiggle Sort II

# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example 1:
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
#
# Example 2:
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?


class Solution(object):
    # 1. sort
    # 2. find mid point
    # 3. take one from end of two lists one by one
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = sorted(nums)
        s = (len(nums) + 1) >> 1
        t = len(nums)
        for i in range(len(nums)):
            if i & 1 == 0:  # even number
                s -= 1
                nums[i] = tmp[s]
            else:           # odd number
                t -= 1
                nums[i] = tmp[t]

sol = Solution()
nums = [1, 5, 1, 1, 6, 4]
sol.wiggleSort(nums)
print(nums)
