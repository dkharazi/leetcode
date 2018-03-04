# -*- coding: utf-8 -*-
"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3757238.html
    # dfs
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, valuelist + [nums[i]])

        # nums.sort()
        res = []
        dfs(0, 0, [])
        return res

    # https://shenjie1993.gitbooks.io/leetcode-python/078%20Subsets.html
    # recursive
    def subsets(self, nums):
        """
        与 Combinations 是一类题目，都可以用递归来解决。
        递归是倒过来解决问题，要求n的情况，就要先求n-1。
        在这里尝试顺序的来解决，通过不断迭代的方法来求所有的子集。
        现在举个例子，集合[1]有[[],[1]]两个子集，
        当向其中添加一个元素时，[1,2]有[[],[1],[2],[1,2]]四个子集，
        可以看出来，
        ，是在原来子集的基础上，
        添加原子集中所有元素加上新元素的总集合。
        为了每个子集中的元素都是不降序的，要先把所有元素都排序。
        """
        res = [[]]
        # looks no need to sort the array
        # for num in sorted(nums):
        for num in nums:
            res += [item + [num] for item in res]
        return res


if __name__ == '__main__':
    print Solution().subsets([1, 4, 3])
