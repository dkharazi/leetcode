# 165. Compare Version Numbers
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
#
# For instance, 2.5 is not "two and a half" or "half way to version three",
# it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        nums1 = list(map(int, version1.split(".")))
        nums2 = list(map(int, version2.split(".")))
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            nums2 += [0] * (len1 - len2)
        else:
            nums1 += [0] * (len2 - len1)

        for i in map(lambda x, y: x - y, nums1, nums2):
            if i > 0:
                return 1
            elif i < 0:
                return -1
        return 0

    # http://bookshadow.com/weblog/2014/12/17/leetcode-compare-version-numbers/
    # w/o map
    def compareVersion(self, version1, version2):
        v1Arr = version1.split(".")
        v2Arr = version2.split(".")
        len1 = len(v1Arr)
        len2 = len(v2Arr)
        for i in range(max(len1, len2)):
            v1Token = 0
            v2Token = 0
            if i < len1:
                v1Token = int(v1Arr[i])
            if i < len2:
                v2Token = int(v2Arr[i])
            if v1Token > v2Token:
                return 1
            if v1Token < v2Token:
                return -1
        return 0


if __name__ == '__main__':
    print Solution().compareVersion("1.0", "1")
    print Solution().compareVersion("01", "1")  # >>> int('01') == 1

    vers = ['0.1', '1.2', '1.1', '0.1', '13.37']
    print sorted(vers, cmp=Solution().compareVersion)

