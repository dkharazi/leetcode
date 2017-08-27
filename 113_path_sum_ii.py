# 113. Path Sum II
#
#  Given a binary tree and a sum,
#  find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
# http://www.tangjikai.com/algorithms/leetcode-112-path-sum
# dfs to track each path

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, sum, res, [])
        return res

    def dfs(self, root, sum, res, path):
        if not root:
            return[]
        if not root.left and not root.right and sum == root.val:
            res.append(path + [root.val])
        self.dfs(root.left, sum - root.val, res, path + [root.val])
        self.dfs(root.right, sum - root.val, res, path + [root.val])

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    print Solution().pathSum(root, 22)
