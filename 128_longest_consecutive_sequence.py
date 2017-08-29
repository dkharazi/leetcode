# -*- coding: utf-8 -*-
# 128. Longest Consecutive Sequence
#
# Given an unsorted array of integers,
# find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#


class Solution(object):
    # brutal force. tle
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(sorted(set(nums)))
        print nums
        if len(nums) == 0:
            return 0

        longest = 1
        for i in range(len(nums)):
            count = 1
            for j in range(i, len(nums) - 1):
                # print nums[j + 1] - nums[j]
                if nums[j + 1] - nums[j] == 1:
                    count += 1
                else:
                    break
            if longest < count:
                longest = count
                # print count

        return longest

    def longestConsecutive(self, nums):
        """
        http://www.cnblogs.com/zuoyuan/p/3765546.html
        解题思路：
        使用一个哈希表，在Python中是字典dict数据类型。
        dict中的映射关系是{x in num：False}，这个表示num中的x元素没有被访问过，
        如果被访问过，则为True。
        如果x没有被访问过，检查x+1，x+2...，x-1，x-2是否在dict中，
        如果在dict中，就可以计数。
        最后可以求得最大长度。

        :param nums:
        :return:
        """
        if not nums:
            return 0

        dict = {x: False for x in nums}
        maxLen = -1
        for num in dict:
            if dict[num] is False:
                dict[num] = True
                curr = num + 1
                lenright = 0
                while curr in dict:
                    lenright += 1
                    dict[curr] = True
                    curr += 1

                curr = num - 1
                lenleft = 0
                while curr in dict:
                    lenleft += 1
                    dict[curr] = True
                    curr -= 1
                maxLen = max(maxLen, lenleft + lenright + 1)
        return maxLen


if __name__ == '__main__':
    print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    print Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
    print Solution().longestConsecutive([1, 2, 0, 1])
