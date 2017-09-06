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

    def majorityElement2(self, num):
        idx, cnt = 0, 1

        for i in xrange(1, len(num)):
            if num[idx] == num[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return num[idx]

    def majorityElement3(self, nums):
        import collections
        if collections.Counter(nums).most_common()[0][1] > len(nums)/2 :
            return collections.Counter(nums).most_common()[0][0]

if __name__ == '__main__':
    print Solution().majorityElement([1, 2, 2, 2, 3])
    print Solution().majorityElement3([1, 1, 2, 1])
    print Solution().majorityElement3([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])

