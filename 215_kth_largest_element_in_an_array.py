# 215. Kth Largest Element in an Array
#
# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 =< k <= array's length.
#

# http://bookshadow.com/weblog/2015/05/23/leetcode-kth-largest-element-array/


import random
import heapq

from random import randint

class Solution(object):
    # nlog(n)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # return sorted(nums)[::-1][k - 1]
        return sorted(nums, reverse=True)[k - 1]

    # quick sort. O(n)
    # https://gengwg.blogspot.com/2017/09/quickselect.html
    def findKthLargest(self, nums, k):
        # randomly chose a pivot within nums
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        # split into a pile nums1 of larger elements and nums2 of smaller elements
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
            # else do nothing

        if k <= len(nums1):
            # it is in the pile of larger elements
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            # it is in the pile of smaller elements
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot

    # heapq
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


    # binary search
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = self.PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1

    def PartitionAroundPivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in xrange(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1

        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx

if __name__ == '__main__':
    print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
