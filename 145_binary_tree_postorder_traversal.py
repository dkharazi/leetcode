# -*- coding: utf-8 -*-
# 145. Binary Tree postorder Traversal
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorder(root, res)
        return res

    def postorder(self, root, values):
        if root:
            self.postorder(root.left, values)
            self.postorder(root.right, values)
            values.append(root.val)

    # iterative
    # https://shenjie1993.gitbooks.io/leetcode-python/145%20Binary%20Tree%20Postorder%20Traversal.html
    # 二叉树进行后序遍历时， 先后序遍历左子树，再后序遍历右子树，最后访问该节点。
    # 也就是说第一次遍历到一个节点的时候，我们不将其加入到结果中，
    # 只有当它的左右子树都遍历完后，我们将该节点加入到结果中。
    # 跟先序遍历中一样，我们也通过栈来解决，把接下去要访问的节点压入栈中。
    # 由于现在每个节点都要遍历两次，我们给节点添加一个标志位，
    # 如果一个节点还没有访问过，我们给的标志为visit，表示下一次遇到它只是第一次访问它，
    # 在访问它之后，我们把它的标志改为get并再次压栈，表示下一次遇到它要访问它的值。
    # 同时还要将它的右子树和左子树分别压栈，表示要后续遍历左子树和右子树。
    # 对于第二次访问的节点，将其加入结果中。
    def postorderTraversal2(self, root):
        result = []  # List[int] stores tree node values
        stack = [(root, 'visit')]  # List[TreeNode]
        while stack:
            node, label = stack.pop()
            if label == 'visit':
                stack.append((node, 'get'))
                if node.right:
                    stack.append((node.right, 'visit'))
                if node.left:
                    stack.append((node.left, 'visit'))
            else:
                result.append(node.val)

        return result


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)

    print Solution().postorderTraversal(root)
    print Solution().postorderTraversal2(root)
