#  230. Kth Smallest Element in a BST
#
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
# How would you optimize the kthSmallest routine?

class Solution(object):
    # iterative
    def kthSmallest(self, root, k):
        # in-order traversal: left->root->right
        # http://bookshadow.com/weblog/2015/07/02/leetcode-kth-smallest-element-bst/
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 0
        while stack and x < k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val

    # https://www.youtube.com/watch?v=CfNRc82ighw
    def kthSmallest(self, root, k):
        # global variables
        self.res = 0
        self.k = k

        def dfs(root):
            # exit condition
            if root is None:
                return
            dfs(root.left)
            # decrement k each time until 0
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            dfs(root.right)

        dfs(root)
        return self.res

    # same as above, but use separate method
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = 0
        self.k = k
        self.inorder(root)
        return self.res

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.inorder(node.right)

    # inorder traversal and put vals into a list
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.inorder(root, res)
        return res[k-1]

    def inorder(self, node, valuelist):
        if not node:
            return
        self.inorder(node.left, valuelist)
        valuelist.append(node.val)
        self.inorder(node.right, valuelist)
