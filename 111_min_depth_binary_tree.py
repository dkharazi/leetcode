# -*- coding: utf-8 -*-
# 111. Minimum Depth of Binary Tree
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
#
# http://www.cnblogs.com/zuoyuan/p/3722045.html
# 解题思路：
# 分几种情况考虑：
# 1，树为空，则为0。
# 2，根节点如果只存在左子树或者只存在右子树，
# 则返回值应为左子树或者右子树的（最小深度+1）。
# 3，如果根节点的左子树和右子树都存在，
# 则返回值为（左右子树的最小深度的较小值+1）。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        if root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    print Solution().minDepth(root)

    root.left.right = TreeNode(2)
    print Solution().minDepth(root)
