# 325 Maximum Size Subarray Sum Equals k

# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
# If there isn't one, return 0 instead.
#
# Example 1:
#
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
#
# Example 2:
#
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
#
# Follow Up:
# Can you do it in O(n) time?

class Solution(object):
    # http://www.voidcn.com/article/p-pbvzylrp-qp.html
    def maxSubArrayLen(self, nums, k):
        res = 0
        acc = 0
        # 累加为0需要先填写，否则中间段出现的0的话，就会值计算从中间段开始的index，
        # 而出现0的话应该从头计算，因为之前的所有加起来刚好是0，需要补充到最大的subarray里。
        d = {0: -1}
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in d:
                d[acc] = i
            if acc - k in d:
                res = max(res, i - d[acc-k])
        return res

print(Solution().maxSubArrayLen(nums = [1, -1, 5, -2, 3], k = 3))
print(Solution().maxSubArrayLen(nums = [-2, -1, 2, 1], k = 1))
