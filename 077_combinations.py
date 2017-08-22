"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    res.append([i, j, k])

        return res

    # http://blog.csdn.net/aliceyangxi1987/article/details/50477505
    # dfs
    def combine(self, n, k):
        ans = []
        self.count = 0

        def dfs(start, nums):
            if self.count == k:
                ans.append(nums)
                return

            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, nums + [i])
                self.count -= 1

        dfs(1, [])

        return ans


if __name__ == '__main__':
    print Solution().combine(4, 2)
