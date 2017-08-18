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

"""

import itertools


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

        # return list(itertools.permutations(nums))


if __name__ == '__main__':
    print Solution().permute([1, 2, 3])
