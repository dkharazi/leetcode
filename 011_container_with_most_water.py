"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).

n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

https://github.com/gengwg/leetcode
"""
class Solution(object):
    # brutal force
    # loop over all heights, calculate all possible areas
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxcontainer = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if maxcontainer < (j - i) * min(height[i], height[j]):
                    maxcontainer = (j - i) * min(height[i], height[j])

        return maxcontainer

    # http://www.cnblogs.com/zuoyuan/p/3779485.html
    def maxArea(self, height):
        left = 0;
        right = len(height) - 1
        res = 0
        # move pointer from both directions
        while left < right:
            # 两个隔板的矮的那一个的高度乘以两个隔板的间距就是储水量
            water = min(height[left], height[right]) * (right - left)
            if water > res:
                res = water
            # always move the lower height
            # because distance is closer, it is only possible larger
            # when the min height is higher
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    print Solution().maxArea([3, 2, 2])
    print Solution().maxArea([3, 5, 7, 4, 2, 9, 12])
