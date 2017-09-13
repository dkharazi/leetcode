# -*- coding: utf-8 -*-
# 199. Binary Tree Right Side View
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-right-side-view.py
# 二叉树的层次遍历，每层按照从右向左的顺序依次访问节点


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # DFS
    def rightSideView(self, root):
        res = []
        self.rightSideViewDFS(root, 1, res)
        return res

    def rightSideViewDFS(self, node, depth, result):
        if not node:
            return

        if depth > len(result):
            result.append(node.val)

        self.rightSideViewDFS(node.right, depth + 1, result)
        self.rightSideViewDFS(node.left, depth + 1, result)

    # BFS
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        result = []
        current_level = [root]

        while current_level:
            # append the last (right-most) value to result.
            result.append(current_level[-1].val)
            # clean next_level so that it only stores current level
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    result = Solution().rightSideView(root)
    print result
