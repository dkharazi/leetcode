# 303. Range Sum Query - Immutable

# Given an integer array nums,
# find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:

# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

# Note:

#     You may assume that the array does not change.
#     There are many calls to sumRange function.

# http://bookshadow.com/weblog/2015/11/10/leetcode-range-sum-query-immutable/
# 计算辅助数组sums：

# sums[0] = 0, for k = 0
# sums[k] = nums[0] + nums[1] + ... + nums[k-1], for k > 0

# 则sumRange(i, j) = sums[j+1] - sums[i]

# e.g.
# sums[5] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
# sums[2] = nums[0] + nums[1]
# sumRange(2,4) = sums[5] - sums[2] = nums[2] + nums[3] + nums[4]

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        size = len(nums)
        self.sums = [0] * (size + 1)
        for i in range(size):
            self.sums[i+1] = self.sums[i] + nums[i]
        # for i in range(1, size+1):
        #     self.sums[i] = self.sums[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
