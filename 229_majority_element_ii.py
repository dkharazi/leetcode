# 229. Majority Element II
#
# Given an integer array of size n,
# find all elements that appear more than n/3  times.
# The algorithm should run in linear time and in O(1) space.
#
# http://bookshadow.com/weblog/2015/06/29/leetcode-majority-element-ii/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = n2 = None
        c1 = c2 = 0
        for n in nums:
            if n1 == n:
                c1 += 1
            elif n2 == n:
                c2 += 1
            elif c1 == 0:
                n1, c1 = n, 1
            elif c2 == 0:
                n2, c2 = n, 1
            else:
                c1, c2 = c1 - 1, c2 - 1
        size = len(nums)
        return [n for n in (n1, n2)
                if n is not None and nums.count(n) > size / 3]

