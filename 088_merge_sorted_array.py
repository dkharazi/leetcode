# -*- coding: utf-8 -*-
"""
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space
(size that is greater or equal to m + n)
to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.


http://blog.csdn.net/coder_orz/article/details/51681144

既然要合并到nums1中，则从合并后nums1的尾部元素开始，
依次向前确定每个元素的值应该是多少。程序需要用到三个指针。

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, q, k = m - 1, n - 1, m + n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[k] = nums1[p]
                p, k = p - 1, k - 1
            else:
                nums1[k] = nums2[q]
                q, k = q - 1, k - 1

        # in case nums2 is longer than nums1
        # move everything left in nums2 to nums1
        nums1[:q + 1] = nums2[:q + 1]

    def merge(self, nums1, m, nums2, n):
        p, q = m - 1, n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[p + q + 1] = nums1[p]
                p -= 1
            else:
                nums1[p + q + 1] = nums2[q]
                q -= 1
        nums1[:q + 1] = nums2[:q + 1]


if __name__ == '__main__':
    nums1 = [1, 3, 5, 7, 11] + 3 * [0]
    Solution().merge(nums1, 5, [4, 6, 9], 3)
    print nums1
