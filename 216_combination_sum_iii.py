# 216. Combination Sum III
#
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
#
# see prob 40. Just add extra constraint len==k.


class Solution(object):
    def dfs(self, candidates, target, start, k, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.ret and len(valuelist) == k:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i + 1, k, valuelist + [candidates[i]])

    def combinationSum3(self, k, n):
        Solution.ret = []
        # candidates is now [1, 2, ..., 9]
        self.dfs(range(1, 10), n, 0, k, [])
        return Solution.ret


if __name__ == '__main__':
    print Solution().combinationSum3(3, 9)
