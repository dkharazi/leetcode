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
    """
    def maxSubArray(self, A):
        #max_ending_here = max_so_far = 0
        #for x in A:
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    ## Brutal force solution
    def maxSubArray(self, A):
        return max([sum(i) for i in self.sublists(A)])

    # enumerate all sub lists...
    def sublists(self, A):
        return [A[m:n+1] for m in range(0,len(A)+1) for n in range(m,len(A)+1)]

if __name__ == "__main__":
    # A = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    #print Solution().maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5])
    #print Solution().maxSubArray([2,1,3,4,1,2,1,5,4])
