# -*- coding: utf-8 -*-
"""
46. Permutations

Given a collection of distinct numbers,
return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

递归（Recursion）

记传入数组为nums，若nums的长度不大于1，则直接返回[nums]

遍历nums，从中抽取一个数num，递归计算剩余数字组成的数组n，然后将num与结果合并
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3758816.html
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            # permute rest of elements
            for perm in self.permute(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + perm)
        return res

        # import itertools
        # return list(itertools.permutations(nums))

    # http://bookshadow.com/weblog/2016/09/09/leetcode-permutations/
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        res = []
        for i, n in enumerate(nums):
            x = nums[:i] + nums[i+1:]
            for p in self.permute(x):
                res.append(p + [n])
        return res


if __name__ == '__main__':
    print Solution().permute([1, 2, 3])
