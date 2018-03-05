# 209. Minimum Size Subarray Sum
#
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum >= s.
# If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        min = len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i:j]) >= s and min > j - i:
                    min = j - i
                    break
        return min
        # return min(minarr, key=lambda x: x[1] - x[0])

    # http://bookshadow.com/weblog/2015/05/12/leetcode-minimum-size-subarray-sum/
    # sliding window.
    # if smaller move end, if larger move start

    def minSubArrayLen(self, s, nums):
        size = len(nums)
        start, end, sum = 0, 0, 0
        bestAns = size + 1
        while end < size:
            while end < size and sum < s:
                sum += nums[end]
                end += 1
            while start < end and sum >= s:
                bestAns = min(bestAns, end - start)
                sum -= nums[start]
                start += 1
        return [0, bestAns][bestAns <= size]

    def minSubArrayLen(self, s, nums):
        size = len(nums)
        start, end, sum = 0, 0, 0
        bestAns = size + 1
        while True:
            if sum < s:
                if end >= size:
                    break
                sum += nums[end]
                end += 1
            else:
                if start > end:
                    break
                bestAns = min(bestAns, end - start)
                sum -= nums[start]
                start += 1
        # return [0, bestAns][bestAns <= size]
        # alternatively use
        return 0 if bestAns == size+1 else bestAns

    # https://gengwg.blogspot.com/2018/03/leetcode-209-minimum-size-subarray-sum.html
    def minSubArrayLen(self, s, nums):
        sz = len(nums)
        minlen = sz + 1    # not possible
        sum = 0
        left =0            # left side of window
        # for i, num in enumerate(nums):
        for i in range(sz):
            sum += nums[i]
            # when current sum reaches s, start deleting from left
            while left <= i and sum >= s:   # can delete left <= i. redundant?
                # record current min length
                minlen = min(minlen, i-left+1)
                sum -= nums[left]
                left += 1
        return 0 if minlen == sz+1 else minlen


if __name__ == '__main__':
    print Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print Solution().minSubArrayLen(4, [1, 4, 4])
    print Solution().minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8])
