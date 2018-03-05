# -*- coding: utf-8 -*-
"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        http://blog.csdn.net/coder_orz/article/details/51363095
        用深度优先搜索（DFS），
        节点的深度与输出结果数组的下标相对应。
        注意在递归的时候要保存每次访问的节点值。
        use preorder traversal to implement level order traversal
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preorder(root, 0, res)
        return res

    def preorder(self, root, level, res):
        # if root is None:
        #     return res
        if root:  # must have!
            # expend res array for next recursion
            if len(res) < level + 1:
                res.append([])
            # append current level subtree root value
            res[level].append(root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)

    # use queue
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        queue = [root]  # store nodes at next level
        while queue:
            level = []  # store values at each level
            # for i, _ in enumerate(queue): # wrong
            for _ in range(len(queue)):
                x = queue.pop(0)
                level.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            res.append(level)
        return res
