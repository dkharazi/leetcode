"""
53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

https://github.com/gengwg
"""


class Solution:
    """
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    http://www.algorithmist.com/index.php/Kadane's_Algorithm

    Kadane's algorithm begins with a simple inductive question:
    if we know the maximum subarray sum ending at position i,
    what is the maximum subarray sum ending at position i+1?

    The answer turns out to be relatively straightforward:
    either the maximum subarray sum ending at position i+1
    includes the maximum subarray sum ending at position i as a prefix,
    or it doesn't.

    Thus, we can compute the maximum subarray sum ending at position i
    for all positions i by iterating once over the array.
    As we go, we simply keep track of the maximum sum we've ever seen.
    """

    # http://www.cnblogs.com/zuoyuan/p/3781988.html
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        ThisSum = 0
        MaxSum = -10000

        for x in A:
            if ThisSum < 0:
                ThisSum = 0
            ThisSum = ThisSum + x
            MaxSum = max(ThisSum, MaxSum)

        return MaxSum

    # variant of above
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = A[0]
        maxsum = A[0]
        for x in A[1:]:
            if cursum < 0:
                cursum = 0
            cursum = cursum + x
            maxsum = max(maxsum, cursum)
        return maxsum

    # Brutal force solution
    def maxSubArray(self, A):
        return max([sum(i) for i in self.sublists(A)])

    # enumerate all sub lists...
    def sublists(self, A):
        return [A[m:n + 1] for m in range(0, len(A)) for n in range(m, len(A))]

    def maxSubArray(self, A):
        # max_ending_here = max_so_far = 0
        # for x in A:
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            # max_ending_here = max(x, max_ending_here + x)
            # max_so_far = max(max_so_far, max_ending_here)
            if max_ending_here > 0:
                max_ending_here += x
            else:
                max_ending_here = x

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

        return max_so_far

    # DP
    # https://gengwg.blogspot.com/2018/03/leetcode-53-maximum-subarray.html
    def maxSubArray(self, A):
        dp = [0] * len(A)
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = A[i] + (0 if dp[i-1] < 0 else dp[i-1])
        return max(dp)


if __name__ == "__main__":
    # A = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # print Solution().maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5])
    # print Solution().maxSubArray([2,1,3,4,1,2,1,5,4])
    # print Solution().sublists([-1, 2, 3])
