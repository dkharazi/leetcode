"""
47. Permutations II

Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3758881.html
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        # must sort array to compare with previous number!
        nums.sort()
        res = []
        prev_num = None
        for i in range(len(nums)):
            # exclude duplicate numbers
            if nums[i] == prev_num:
                continue
            prev_num = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + j)
        return res


if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 2])
