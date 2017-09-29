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

if __name__ == '__main__':
    print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
