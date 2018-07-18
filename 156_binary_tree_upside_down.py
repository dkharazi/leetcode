# 156. Binary Tree Upside Down

# Given a binary tree where all the right nodes are either leaf nodes with a sibling
# (a left node that shares the same parent node) or empty,
# flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes.
# Return the new root.

# For example:
# Given a binary tree {1,2,3,4,5},
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# return the root of the binary tree [4,5,2,#,#,3,1].
#
#    4
#   / \
#  5   2
#     / \
#    3   1
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

# https://zhuhan0.blogspot.com/2017/05/leetcode-156-binary-tree-upside-down.html
#
# Thought process:
# After the flip, root and root.right will become siblings, and the left most child will become the new root.
# The idea is to traverse the tree to the left. As we traverse, we make root.left the new root,
# root.right the left child of new root, and root itself the right child of new root.

class Solution:
    def upsideDownBinaryTree(self, root):
        if root is None or root.left is None:
            return root

        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None

        return left


