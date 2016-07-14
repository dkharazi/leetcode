#
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7]
# is rotated to [5,6,7,1,2,3,4].
#

class Solution:
    def rotate(self, nums, n):
        return nums[-n:] + nums[:-n]
        # for right rotate use below
        # return l[n:] + l[:n]

if __name__ == "__main__":
    print Solution().rotate([1,2,3,4,5,6,7], 3)

    # this can also be applied to strings
    s = "abcdefg"
    print Solution().rotate(s, 3)

