# 276 Paint Fence

# There is a fence with n posts, each post can be painted with one of the k colors.
#
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
#
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.

class Solution():
    # https://www.cnblogs.com/airwindow/p/4796688.html

    # The problem of asking how many ways to do something is usually very easy!
    # And it could always be solved through dynamic programming.
    # You just need to carefully design the transitional function acoording to characteristics
    # or certain restrictions.

    # We know for each post, it could differ or same as its previous post's color.
    # Assume:
    # differ_count: represents the current post with different color with its previous post (the painting ways)
    # same_count: represents the current post share the same color with its previous post (the painiting ways)

    # We could have following trasitinao function
    # differ_count(i) = differ_count(i-1) * (k-1) + same_count(i-1) * (k-1)
    # same_count(i) = differ_count(i-1)
    # //cause the current post must have the same color with post i-1,
    # thus we could only use the way that differ_count(i-1)

    # Base case:
    # 2 is a perfect base case for use to start, since it has simple same_count and differ_count;
    def numWays(self, n , k ):
        if n <= 0:
            return 0
        if n == 1:
            return k

        # n == 2
        same = k
        diff = k*(k-1)

        for i in range(3, n+1):
            tmp = diff
            diff = same * (k-1) + diff * (k-1)
            same = tmp

        # for i in range(3, n+1):
        #     same, diff = diff , same*(k-1) + diff*(k-1)

        return same + diff


test= Solution()
print test.numWays(5,2)

