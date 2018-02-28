# -*- coding: utf-8 -*-
"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3699449.html
    # 使用一个变量mindiff来监测和与target之间的差值，如果差值为0，直接返回sum值。
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # sort modifies original list
        nums.sort()  # n log(n)
        mindiff = 100000
        res = 0

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if sum == target:  # use sum not res here.
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return res

    # https://gengwg.blogspot.com/2018/02/leoleetcode-16-sum-closest-letter.html
    # use sys.maxsize, enumerate
    def threeSumClosest(self, nums, target):
        import sys
        nums.sort()
        res = 0
        mindiff = sys.maxsize
        for index, a in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                total = a + b + c
                diff = abs(total - target)
                if diff < mindiff:
                    mindiff = diff
                    res = total
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    print Solution().threeSumClosest([-1, 2, 1, -4], 1)  # 2
