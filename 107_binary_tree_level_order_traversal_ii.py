"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # same as 102. just add reverse the result.
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preorder(root, 0, res)

        # this not work, because reverse() modifies list in place, returns null.
        # ans = res.reverse()
        res.reverse()

        # this not work, because reversed() returns list_reverseiterator not a list.
        # return reversed(res)
        return res

    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)

    # not using reverse
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preorder(root, 0, res)
        return res

    def preorder(self, root, level, res):
        if root:
            if len(res) <= level:
                res.insert(0, [])
            res[len(res)-level-1].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)

    # use queue
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        queue = [root]  # store nodes at next level
        while queue:
            level = []  # store values at each level
            for _ in range(len(queue)):
                x = queue.pop(0)
                level.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            res.insert(0,level)
        return res
~
