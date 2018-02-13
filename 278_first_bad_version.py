# 278. First Bad Version
#
# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, 
# all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] 
# and you want to find out the first bad one, 
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. 
# Implement a function to find the first bad version. 
# You should minimize the number of calls to the API. 


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n + 1  
        l, r = 1, n + 1
        while l < r:
            # mid = (l + r) / 2
            mid = l + ((r-l) >> 1)
            if isBadVersion(mid):   # first bad is on the left half
                r = mid
            else:   # first bad is on the right half
                l = mid + 1
        return l
        
    def firstBadVersion(self, n):
        l, r = 1, n+1
        while l + 1 < r:    # this way l, r just set to mid
            mid = l + ((r-l) >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        # need check which of l, r  is bad
        return l if isBadVersion(l) else r