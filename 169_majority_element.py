# -*- coding: utf-8 -*-
# 169. Majority Element
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty
# and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for num in dict:
            if dict[num] > len(nums) / 2:
                return num

    # http://www.tangjikai.com/algorithms/leetcode-169-majority-element
    # Sort it and then return the middle element.
    def majorityElement(self, nums):
        return sorted(nums)[len(nums) / 2]

    # http://bookshadow.com/weblog/2014/12/22/leetcode-majority-element/
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    def majorityElement(self, nums):
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate, count = num, 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    print Solution().majorityElement([1, 2, 2, 2, 3])
