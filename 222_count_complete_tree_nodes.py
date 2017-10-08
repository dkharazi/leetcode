# 222. Count Complete Tree Nodes
#
# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Get the depth of child node to get the number of nodes.
        http://www.tangjikai.com/algorithms/leetcode-222-complete-tree-nodes
        """
        if self.getDepth(root, True) == self.getDepth(root, False):
            return int(pow(2, self.getDepth(root, True))) - 1
        else:
            return self.countNodes(root.left)

    def getDepth(self, root, isLeft):
        level = 0
        while root:
            if isLeft:
                root = root.left
            else:
                root = root.right
            level += 1
        return level


