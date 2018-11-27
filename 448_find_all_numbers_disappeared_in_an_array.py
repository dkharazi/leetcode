# 448. Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initialize a hashmap of 1..n with value 0
        cmap = {i:0 for i in range(1, len(nums)+1)}

        # store the count of each number in nums
        for num in nums:
            cmap[num] += 1

        res = []
        # those num with count zero are missing from 1..n
        for k in cmap:
            if cmap[k] == 0:
                res.append(k)
        return res

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
