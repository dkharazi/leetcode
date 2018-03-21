# 153. Find Minimum in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.


class Solution(object):
    # http://bookshadow.com/weblog/2014/10/16/leetcode-find-minimum-rotated-sorted-array/
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            # if nums[m] <= nums[r]:
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

    # http://www.cnblogs.com/zuoyuan/p/4045742.html
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r and nums[l] > nums[r]:
            m = (l + r) / 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


if __name__ == '__main__':
    print Solution().findMin([4, 5, 6, 7, 0, 1, 2])
