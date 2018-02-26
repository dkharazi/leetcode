# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i

if __name__ == '__main__':
    print "index1={0}, index2={1}".format(*Solution().twoSum((2, 7, 11, 15), 9))
    print "index1={0}, index2={1}".format(*Solution().twoSum((2, 11, 15, 7), 9))
