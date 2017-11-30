# 228. Summary Ranges
#
# Given a sorted integer array without duplicates,
# return the summary of its ranges.
#
# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
#
# http://bookshadow.com/weblog/2015/06/26/leetcode-summary-ranges/
# convert all increasing series into (start-->end)


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i, size = 0, len(nums)
        ans = []
        while i < size:
            c, r = i, str(nums[i])
            while i + 1 < size and nums[i + 1] - nums[i] == 1:
                i += 1
            if i > c:
                r += '->' + str(nums[i])
            ans.append(r)
            i += 1
        return ans


if __name__ == "__main__":
    print Solution().summaryRanges([0,1,2,4,5,7])
