# 152. Maximum Product Subarray
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution:
    def maxProduct(self, A):
        """
        http://www.cnblogs.com/zuoyuan/p/4019326.html
        :param A:
        :return:
        """
        # if len(A) == 0:
        #    return 0

        min_tmp = A[0]
        max_tmp = A[0]
        result = A[0]
        for i in range(1, len(A)):
            # must save tmp max/min to variable. otherwise not using current max/min.
            a = A[i] * min_tmp
            b = A[i] * max_tmp
            c = A[i]
            min_tmp = min(min(a, b), c)
            max_tmp = max(max(a, b), c)
            result = max_tmp if max_tmp > result else result
        return result

    # https://gengwg.blogspot.com/2018/03/leetcode-152-maximum-product-subarray.html
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mintmp = nums[0]
        maxtmp = nums[0]
        res = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            tmp = mintmp
            mintmp = min(num * mintmp, num * maxtmp, num)
            maxtmp = max(num * tmp, num * maxtmp, num)
            res = max(maxtmp, res)
        return res

if __name__ == '__main__':
    print Solution().maxProduct([2, 3, 1, 4, 7, -2, 2])
