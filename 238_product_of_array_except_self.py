# -*- coding: utf-8 -*-
# 238. Product of Array Except Self
#
# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution(object):
    # use division
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = reduce(lambda x, y: x * y, nums)
        return [prod/n for n in nums]

    # TLE
    def productExceptSelf(self, nums):
        return [reduce(lambda x, y: x * y, (nums[:i] + nums[(i+1):])) for i in range(len(nums))]

    # http://bookshadow.com/weblog/2015/07/16/leetcode-product-array-except-self/
    # 链接地址：https://leetcode.com/discuss/46104/simple-java-solution-in-o-n-without-extra-space
    # 由于output[i] = (x0 * x1 * ... * xi-1) * (xi+1 * .... * xn-1)
    # 因此执行两趟循环：
    # 第一趟正向遍历数组，计算x0 ~ xi-1的乘积
    # 第二趟反向遍历数组，计算xi+1 ~ xn-1的乘积
    def productExceptSelf(self, nums):
        size = len(nums)
        output = [1] * size
        left = right = 1
        # output: [x3*x2*x1, x3*x2*x0, x3*x1*x0, x2*x1*x0]
        #           1 --> N-1
        # left: [1, x0, x0*x1, x0*x1*x2]
        for i in range(size - 1):
            left *= nums[i]
            output[i + 1] *= left
        #         0 <-- N-2
        # right: [x3*x2*x1, x3*x2, x3, 1]
        for i in range(size - 1, 0, -1):
            right *= nums[i]
            output[i - 1] *= right
        return output


if __name__ == "__main__":
    print Solution().productExceptSelf([1,2,3,4])

