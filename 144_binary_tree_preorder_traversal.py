# -*- coding: utf-8 -*-
# 144. Binary Tree Preorder Traversal
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # recursive
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, values):
        if root:
            values.append(root.val)
            self.preorder(root.left, values)
            self.preorder(root.right, values)

    # iterative
    # https://shenjie1993.gitbooks.io/leetcode-python/144%20Binary%20Tree%20Preorder%20Traversal.html
    # 二叉树进行前序遍历时，首先访问根结点然后遍历左子树，最后遍历右子树。
    # 在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。
    # 可以看出采用递归的方法非常简单，
    # 如果不用递归，我们可以通过一个栈来辅助遍历。
    # 在先序遍历中，访问完根节点，我们接着遍历它的左子树，
    # 它的右子树要等左子树遍历完成后再遍历，所以我们先把它存起来。
    # 而左子树的头节点（区别于根节点）也会有它的右子树，
    # 这棵右子树需要比之前的右子树先遍历（因为它是根节点的左子树中的），
    # 所以存储采用栈的结构。
    # 当遍历到某一个节点没有左子树后，我们从栈中取出右子树节点继续遍历，直到遍历完整棵树。
    def preorderTraversal2(self, root):
        stack = []  # List[TreeNode] stores right tree nodes
        result = []  # List[int] stores tree node values
        while root or stack:
            if not root:
                root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            # note put right in stack first before traversing left!
            root = root.left
        return result


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)

    print Solution().preorderTraversal(root)
    print Solution().preorderTraversal2(root)
