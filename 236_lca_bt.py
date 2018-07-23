# -*- coding: utf-8 -*-
# 236. Lowest Common Ancestor of a Binary Tree
#
#  Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes v and w as the lowest node in T
# that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
#
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
# Another example is LCA of nodes 5 and 4 is 5,
# since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://www.hrwhisper.me/algorithm-lowest-common-ancestor-of-a-binary-tree/
# https://articles.leetcode.com/lowest-common-ancestor-of-a-binary-tree-part-i/

# A Bottom-up Approach (Worst case O(n) ):

# Using a bottom-up approach, we can improve over the top-down approach by avoiding traversing the same nodes over and over again.
#
# We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its parent.
# The parent would then test its left and right subtree if each contain one of the two nodes.
# If yes, then the parent must be the LCA and we pass its parent up to the root.
# If not, we pass the lower node which contains either one of the two nodes (if the left or right subtree contains either p or q),
# or NULL (if both the left and right subtree does not contain either p or q) up.
#
# Sounds complicated? Surprisingly the code appears to be much simpler than the top-down one.

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None
