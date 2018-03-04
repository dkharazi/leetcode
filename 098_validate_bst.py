# -*- coding: utf-8 -*-
"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.

Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.


http://www.cnblogs.com/slurm/p/5221590.html

递归：棵树是二叉查找树，
那么左子树的节点值一定处于（负无穷，root.val）这个范围内，
右子树的节点值一定处于（root.val，正无穷）这个范围内。
（注意边界值，负无穷和正无穷换成浮点型的极值）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTRecur(root, float("-inf"), float("inf"))

    def isValidBSTRecur(self, node, min, max):
        if node is None:
            return True

        if node.val <= min or node.val >= max:
            return False

        return self.isValidBSTRecur(node.left, min, node.val) and \
               self.isValidBSTRecur(node.right, node.val, max)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print Solution().isValidBST(root)
