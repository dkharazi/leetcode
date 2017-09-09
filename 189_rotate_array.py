# -*- coding: utf-8 -*-
# 189. Rotate Array
#
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.


class Solution:
    def rotate(self, nums, n):
        return nums[-n:] + nums[:-n]
        # for right rotate use below
        # return l[n:] + l[:n]

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        a = nums[-k:] + nums[:-k]
        for i in range(len(a)):
            nums[i] = a[i]

    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

    # https://shenjie1993.gitbooks.io/leetcode-python/189%20Rotate%20Array.html
    # 解法一，记下最后一个数字，其他的数字向后移一位，最后把记下的数字放在开头，如此进行k次。
    # 这个解法空间复杂度为O(1)，时间复杂度O(kn)。
    #
    # 解法二，申请一个等大的数组，将移位后的结果存在新申请的数组中。
    # 这个解法空间复杂度为O(n)，时间复杂度为O(n)。
    #
    # 解法三，右旋k个数字有个等价操作，就是将前k个数字翻转，将剩下的数字也翻转，最后将整个数组翻转。
    # 此时数组与右旋k个数字的结果相同。这个解法空间复杂度为O(1)，时间复杂度为O(n)。
    #
    # 注意，k可能比数组的长度n还大，我们可以将k对n取余数，因为右旋n个数字相当于没有变化，可以减少计算量。

    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    print Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)

    # this can also be applied to strings
    # s = "abcdefg"
    # print Solution().rotate(s, 3)
