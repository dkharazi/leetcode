# -*- coding: utf-8 -*-
# 114. Flatten Binary Tree to Linked List
#
#  Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# click to show hints.
#
# Hints:
# If you notice carefully in the flattened tree,
# each node's right child points to the next node of a pre-order traversal.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        http://www.cnblogs.com/zuoyuan/p/3721157.html

        解题思路：
        首先将左右子树分别平化为链表，
        这两条链表的顺序分别为左子树的先序遍历和右子树的先序遍历。
        然后将左子树链表插入到根节点和右子树链表之间，就可以了。
        左右子树的平化则使用递归实现。

        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if p.left is None:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None

    def flatten(self, root):
        """
        https://shenjie1993.gitbooks.io/leetcode-python/114%20Flatten%20Binary%20Tree%20to%20Linked%20List.html
        可以看出来变化后每个节点其实都是指向了在先序遍历中的后一个节点。
        所以就通过栈的方式来先序遍历原树，
        如果一个节点有左节点，那么把它的右节点压栈（如果有的话），右指针指向原来的左节点；
        如果一个节点没有子节点，应该把它的右指针指向栈顶的节点。
        """
        stack = []
        while root:
            if root.left:
                if root.right:
                    stack.append(root.right)
                root.right, root.left = root.left, None
            if not root.right and stack:
                root.right = stack.pop()
            root = root.right
