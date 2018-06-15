# 247 Strobogrammatic Number II

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Find all strobogrammatic numbers that are of length = n.

# For example,
# Given n = 2, return ["11","69","88","96"].

class Solution:
    def findStrobogrammatic(self, n):
        res = []
        if n == 0:
            return res
        if n % 2 == 1:
            res.append('0')
            res.append('1')
            res.append('8')
        else:
            res.append('')
        n  /= 2
        nums1 = ['0', '1', '6', '9', '8']
        nums2 = ['0', '1', '9', '6', '8']
        while n > 0:
            tmp = []
            # do not append 0 if it is last iteration
            start = 1 if n == 1 else 0
            for s in res:
                i = start
                while i < len(nums1):
                    tmp.append(nums1[i] + s + nums2[i])
                    i += 1
            res = tmp   # continue build on top of tmp
            n -= 1
        return res


print Solution().findStrobogrammatic(1)
print Solution().findStrobogrammatic(2)
print Solution().findStrobogrammatic(3)
print Solution().findStrobogrammatic(4)
