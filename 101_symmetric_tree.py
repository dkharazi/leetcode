"""
101 Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        http://www.cnblogs.com/zuoyuan/p/3747174.html

        check if root.left==root.right.
        if equal, check root.left.left==root.right.right && root.left.right==root.right.left

        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, p, q):
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left)
        return False

    # ref 100
    def helper(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.helper(p.left, q.right) and self.helper(p.right, q.left)
