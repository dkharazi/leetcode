# 378. Kth Smallest Element in a Sorted Matrix
#
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
# Note:
# You may assume k is always valid, 1 <= k <= n2.

# https://nb4799.neu.edu/wordpress/?p=2017

from heapq import *

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # heapq.merge: Merge multiple sorted inputs into a single sorted output
        # (for example, merge timestamped entries from multiple log files).
        # Returns an iterator over the sorted values.
        return list(merge(*matrix))[k-1]

    # Maintain a min-heap with k element, initialized by the elements of the first row.
    # Since it is a min-heap, and note the property that rows and columns are already sorted in ascending order,
    # the heap root after popping k-1 times is the k-th smallest element of the whole matrix.
    # When popping the heap, we also need to push necessary matrix elements into the heap.
    # Time complexity is O(KlogK) (every heap operation takes O(logK))
    def kthSmallest(self, matrix, k):
        # element in the heap: (val, x coord, y coord)
        h = []

        for i in range(min(len(matrix[0]), k)):
            heappush(h, (matrix[0][i], 0, i))

        # pop k-1 times
        for i in range(k-1):
            val, x, y = heappop(h)
            if x < len(matrix) - 1:
                heappush(h, (matrix[x+1][y], x+1, y))

        return h[0][0]  # smallest element in heap. 0th index in tuple

    # binary search
    # We can eventually find the k-th smallest element by shrinking the search range in binary search.
    # Binary search is feasible for this problem since left, right,and mid in binary search are integers
    # and we know that matrix elements are integers.

    # The algorithm takes O(nlogN) time (N is the range of matrix[0][0] ~ matrix[n-1][n-1]) and O(1) space.

    # Time complexity analysis: the outer loop executes at most O(logN) times.
    # The inner for loop executes at most O(n) times.
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        L = matrix[0][0]
        R = matrix[n-1][n-1]

        while L < R:
            mid = L + ((R - L) >> 1)
            count = 0
            j = n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j+1
            if count >= k:
                R = mid
            else:
                L = mid + 1
        return L


sol = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(sol.kthSmallest(matrix, k))
