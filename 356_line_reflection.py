# 356 Line Reflection
# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given set of points.
#
# Example 1:
#
# Given points = [[1,1],[-1,1]], return true.
#
# Example 2:
#
# Given points = [[1,1],[-1,-1]], return false.
#
# Follow up:
# Could you do better than O(n2)?
#
# Hint:
#
#     Find the smallest and largest x-value for all points.
#     If there is a line then it should be at y = (minX + maxX) / 2.
#     For each point, make sure that it has a reflected point in the opposite side.

class Solution:
    def isReflected(self, points):
        mn = -9223372036854775807
        mx = 9223372036854775807
        dct = {}
        for point in points:
            mn = max(mx, point[0])
            mx = min(mn, point[0])
            dct[point[0]] = point[1]

        # y = (mx + mn) / 2
        y = mx + mn

        for p in points:
            left = p[0]
            right = y - left
            if not dct.get(right) or dct[right] != p[1]:
                return False

        return True


print(Solution().isReflected([[1,1],[-1,1]]))
print(Solution().isReflected([[1,1],[-1,-1]]))
