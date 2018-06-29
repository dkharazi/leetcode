# LEETCODE 360. SORT TRANSFORMED ARRAY

# Given a sorted array of integers nums and integer values a, b and c.
# Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example:
#
#     nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
#
#     Result: [3, 9, 15, 33]
#
#     nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
#
#     Result: [-23, -5, 1, 7]

class Solution(object):
    # https://github.com/kamyu104/LeetCode/blob/master/Python/sort-transformed-array.py
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        f = lambda x, a, b, c : a*x*x + b*x + c

        res = []
        if not nums:
            return res

        left, right = 0, len(nums) - 1
        d = -1 if a > 0 else 1
        while left <= right:
            if d * f(nums[left], a, b, c) < d * f(nums[right], a, b, c):
                res.append(f(nums[left], a, b, c))
                left += 1
            else:
                res.append(f(nums[right], a, b, c))
                right -= 1

        return res[::d]


print Solution().sortTransformedArray(nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5)
print Solution().sortTransformedArray(nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5)

