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
            a = A[i] * min_tmp
            b = A[i] * max_tmp
            c = A[i]
            min_tmp = min(min(a, b), c)
            max_tmp = max(max(a, b), c)
            result = max_tmp if max_tmp > result else result
        return result


if __name__ == '__main__':
    print Solution().maxProduct([2, 3, 1, 4, 7, -2, 2])
