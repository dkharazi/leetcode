# -*- coding: utf-8 -*-
# 162. Find Peak Element
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# click to show spoilers.
#
# Note:
# Your solution should be in logarithmic complexity.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#

class Solution(object):
    # at peak  nums[i - 1] < nums[i] > nums[i + 1]
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return nums.index(max(nums))

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i

    # binary search
    # https://shenjie1993.gitbooks.io/leetcode-python/162%20Find%20Peak%20Element.html
    #
    #    /\
    #   /  \/\   /\
    #  /      \/   \
    # /             \
    #
    # 从上图可以看出，一条上升的边和一条下降的边之间至少夹着一个顶点元素。
    # 由于左右两边各有一个无穷小的元素，所以起始的时候最左边的边是上升的，最右边的边是下降的。
    # 要求时间复杂度为log(n)，我们可以通过二分搜索来判断。
    # 我们取中点和它后面的一个点，如果这两个点构成的边是上升的，那我们就把中点左边的点抛弃掉，
    # 这时候仍然满足最左边的边是上升的，最右边的边是下降的；
    # 如果两个点构成的边是下降的，那么该把中点右边的点抛弃掉，
    # 这样仍然满足上面的要求，保证左右两个点之间至少有一个顶点元素。
    # 至于如何在两点中选择新的左右节点，我们要尽可能使新的左右节点靠近顶点元素，
    # 因为最终的终止条件是左右节点重合。
    # 所以选择新的左节点时，应该选中点的后一个节点，而选新的右节点时，选择中点。
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    print Solution().findPeakElement([1, 2, 3, 1])
    print Solution().findPeakElement([1, 2])
