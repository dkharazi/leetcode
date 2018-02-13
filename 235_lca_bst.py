# -*- coding: utf-8 -*-
# 235. Lowest Common Ancestor of a Binary Search Tree
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia:
# "The lowest common ancestor is defined between two nodes v and w as the lowest node in T
# that has both v and w as descendants (where we allow a node to be a descendant of itself)."
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
#
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2,
# since a node can be a descendant of itself according to the LCA definition.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# http://www.tangjikai.com/algorithms/leetcode-235-lowest-common-ancestor-of-a-binary-search-tree
# If p.val <= root.val <= q.val or q.val <= root.val <= p.val, it means root is LCA of p and q.
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

        if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestor(self, root, p, q):
        s, b = sorted([p.val, q.val])
        while not s <= root.val <=b:
            root = root.left if s <= root.val else root.right
        return root

if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(0)
    root.right.right = TreeNode(9)
    p = root.left.right
    q = root.left.left
    print Solution().lowestCommonAncestor(root, p, q).val

