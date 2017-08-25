"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

http://www.cnblogs.com/colorss/p/5348284.html
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorder_recursive(root, res)
        return res

    def inorder_recursive(self, root, res):
        if root:
            self.inorder_recursive(root.left, res)
            res.append(root.val)
            self.inorder_recursive(root.right, res)

if __name__ == '__main__':
    # Driver code
    # http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print Solution().inorderTraversal(root)