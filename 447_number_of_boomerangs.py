# 447. Number of Boomerangs
# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k)
# such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points
# are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

# https://leetcode.com/problems/number-of-boomerangs/discuss/92868/Short-Python-O(n2)-hashmap-solution
# for each point, create a hashmap and count all points with same distance.
# If for a point p, there are k points with distance d, number of boomerangs corresponding to that are k*(k-1).
# Keep adding these to get the final result.
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
	# function to calculate distance between two points
        def dis(a, b):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx * dx + dy * dy

        res = 0
        for p in points:
            cmap = {}   # create hashmap inside loop. for each point.
            for q in points:
                d = dis(p, q)
                cmap[d] = cmap.get(d, 0) + 1
            for k in cmap:
                res += cmap[k] * (cmap[k] - 1)
        return res

print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))


