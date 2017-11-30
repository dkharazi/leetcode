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

# http://bookshadow.com/weblog/2015/07/02/leetcode-kth-smallest-element-bst/
# in-order traversal: left->root->right
class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while stack and x <= k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val

# https://www.youtube.com/watch?v=CfNRc82ighw
class Solution(object):
    def kthSmallest(self, root, k):
        # global variables
        self.res = 0
        self.k = k

        def dfs(root):
            # exit condition
            if root is None:
                return 0
            dfs(root.left)
            # decrement k each time until 0
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.right)

        dfs(root)
        return self.res


