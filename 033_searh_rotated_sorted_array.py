"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search.
If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3777422.html
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid

            # eventually target will be located in some ascending sub-sequence
            elif nums[start] <= nums[mid]: # left half in ascending order
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:   # target is not in left half
                    start = mid + 1
            else:       # right half in ascending order
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:   # target not in right half
                    end = mid - 1

        return -1


if __name__ == '__main__':
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 1)
    print Solution().search([], 3)
