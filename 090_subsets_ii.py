"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums,
return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        # need sort array first for remove duplicates
        nums.sort()
        # nums = sorted(nums)
        for num in nums:
            # add one condition to original list comprehension
            res += [[num] + item for item in res if [num] + item not in res]
        return res


if __name__ == '__main__':
    print Solution().subsetsWithDup([1, 2, 3])
    print Solution().subsetsWithDup([4, 4, 4, 1, 4])
