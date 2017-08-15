"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3699449.html
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # sort modifies original list
        nums.sort()
        mindiff = 100000
        res = 0

        for i in range(len(nums)):
            left, right = i + 1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum-target)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == '__main__':
    print Solution().threeSumClosest([-1, 2, 1, -4], 1) # 2
