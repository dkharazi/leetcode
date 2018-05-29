# 300. Longest Increasing Subsequence
#
# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Note that there may be more than one LIS combination,
# it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?


class Solution(object):
    # https://gengwg.blogspot.com/2018/02/leetcode-300-longest-increasing.html
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sz = len(nums)
        dp = [1] * sz
        for i in range(sz):
            for j in range(i):
                if nums[i] > nums[j]:
                    # max of multiple possible sub problems
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))