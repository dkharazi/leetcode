# 117. Populating Next Right Pointers in Each Node II
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
#
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    # https://shenjie1993.gitbooks.io/leetcode-python/117%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II.html
    def connect(self, root):
        dummy = TreeLinkNode(-1)
        node = dummy
        while root:
            while root:
                node.next = root.left
                node = node.next or node
                node.next = root.right
                node = node.next or node
                root = root.next
            root, node = dummy.next, dummy
