# 268. Missing Number
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# Example 1

# Input: [3,0,1]
# Output: 2

# Example 2

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# Note:
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant extra space complexity? 

class Solution(object):
    # 1 + 2 + ... + n = (1+n)n/2
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (1 + len(nums)) * len(nums) / 2 - sum(nums)

A = [3,0,1]
B = [9,6,4,2,3,5,7,0,1]
print Solution().missingNumber(A)
print Solution().missingNumber(B)
