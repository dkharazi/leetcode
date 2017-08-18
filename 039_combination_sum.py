"""
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates)
and a target number (T),
find all unique combinations in C
where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3777540.html
    def dfs(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i, valuelist + [candidates[i]])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.ret = []
        self.dfs(candidates, target, 0, [])
        return Solution.ret

if __name__ == '__main__':
    print Solution().combinationSum([2, 3, 6, 7], 7)