# 368. Largest Divisible Subset

# Given a set of distinct positive integers,
# find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
#
# Example 2:
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]
#

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = [0] * n
        pre = [0] * n
        nums.sort()
        max = 0
        index = -1

        for i in range(n):
            count[i] = 1
            pre[i] = -1
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if 1 + count[j] > count[i]:
                        count[i] = count[j] + 1
                        pre[i] = j
            if count[i] > max:
                max = count[i]
                index = i

        res = []
        while index != -1:
            res.append(nums[index])
            index = pre[index]
        return res

    # https://leetcode.com/problems/largest-divisible-subset/discuss/83999/Easy-understood-Java-DP-solution-in-28ms-with-O(n2)-time
    # 1. Sort
    # 2. Find the length of longest subset
    # 3. Record the largest element of it.
    # 4. Do a loop from the largest element to nums[0], add every element belongs to the longest subset.
    def largestDivisibleSubset(self, nums):
        res = []
        n = len(nums)
        if not nums or n == 0:
            return res
        nums.sort()
        dp = [1] * n # nums fill(dp, 1). 0 not work. every number at least has itself as subset
        # dp[0] = 1

        # for each element in nums, find the largest subset it has
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

        # pick the index of largest element in dp
        maxIndex = 0
        for i in range(1, n):
            #maxIndex = i if dp[i] > dp[maxIndex] else maxIndex
            if dp[i] > dp[maxIndex]:
                maxIndex = i

        # from nums[maxIndex] to nums[0], add every element belongs to the largest subset
        temp = nums[maxIndex]
        curDp = dp[maxIndex]
        for i in range(maxIndex, -1, -1):
            if temp % nums[i] == 0 and dp[i] == curDp: # dpi must be prev - 1
                res.append(nums[i])
                temp = nums[i]  # current num belongs to subset so check next number
                curDp -= 1      # reduce length of subset

        return res


print(Solution().largestDivisibleSubset([1,2,4,8]))
print(Solution().largestDivisibleSubset([1,2,3]))
print(Solution().largestDivisibleSubset([4,8,10,240]))
print(Solution().largestDivisibleSubset([2,3,8,9,27]))
print(Solution().largestDivisibleSubset( [1,2,4,8,9,72] ))
print(Solution().largestDivisibleSubset([3,4,6,8,12,16,32]))
