# -*- coding: utf-8 -*-
"""
60. Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


class Solution(object):
    # itertools.permutations TLE
    def getPermutation(self, n, k):
        import itertools
        return ''.join([str(x) for x in list(itertools.permutations(range(1, n + 1)))[k - 1]])

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1] * (n + 1)

        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i

        nums = [str(x + 1) for x in range(n)]
        ans = ''

        for i in range(n):
            j = (k - 1) / fac[n - i - 1]
            ans += nums[j]
            nums.remove(nums[j])
            k = (k - 1) % fac[n - i - 1] + 1

        # another way
        # k = k - 1
        # for i in range(n, 0, -1):
        #     index = k / fac[i - 1]
        #     k = k % fac[i - 1]
        #     ans += nums[index]
        #     nums.remove(nums[index])

        return ans


if __name__ == '__main__':
    print Solution().getPermutation(6, 40)
    print Solution().getPermutation(8, 15025)
